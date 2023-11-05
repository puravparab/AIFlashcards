from django.conf import settings
from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import openai
from openai.embeddings_utils import get_embedding
openai.api_key = settings.OPEN_AI

import pinecone
pinecone.init(api_key=settings.PINECONE, environment=settings.PINECONE_ENV)

from .models import Document, Text

"""
File upload API
"""
@api_view(['POST'])
def upload_file(request, format=None):
	file = request.data.get("file")
	file_id = create_document_entry(file)
	if file_id:
		return Response({"file_id": file_id}, status=status.HTTP_200_OK)
	else:
		return Response({"error": "error creating document entry"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

"""
Create a entry in the Document table
"""
def create_document_entry(file):
	request = Document.objects.create(
		file = file,
		qa_json = {}
	)
	request.save()
	return request.id

"""
Create and store the embeddings of a file
"""
@api_view(['POST'])
def create_store_embeddings(request, f_id):
	file = request.data.get("file")
	if isinstance(file, InMemoryUploadedFile):
		# Create embeddings
		all_embeddings = []
		file_content = file.read().decode('utf-8')
		count = 0
		for line in file_content.split('\n'):
			if line != "\r":
				embedding = create_embedding(line)
				text_id = create_text_entry(line, f_id)
				all_embeddings.append((str(text_id), embedding, {"id": text_id}))
				print(f'#{count}: {text_id} processed')
				count += 1

		insert_pinecone(settings.PINECONE_INDEX, all_embeddings)


		return Response({"file_id": f_id, "response": response}, status=status.HTTP_200_OK)

	return Response({"error": "error creating document entry"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

"""
Use OpenAI chat completion to create multiple flashcards
"""
@api_view(['POST'])
def chat_completion(request, file):
	file_content = file.read().decode('utf-8')
	# Create flashcards
	response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": "You are a helpful assistant who creates flashcards. Reply in the form [{q: a}, {q: a}, ...] and provide multiple flashcards."},
			{"role": "user", "content": file_content[:500]},
		]
	)
	return Response({"res": response}, status=status.HTTP_200_OK)

"""
Use OpenAI embedding model to create 
"""
def create_embedding(line):
	try:
		embedding = get_embedding(line, engine='text-embedding-ada-002')
		return embedding
	except Exception as e:
		return None

"""
Create a entry in the Text table
"""
def create_text_entry(text, file_id):
	request = Text(
		text = text,
		document = Document.objects.get(id=file_id),
	)
	request.save()
	return request.id

"""
Add to pinecone vector DB
"""
def insert_pinecone(index, embeddings):
	index = pinecone.Index(index)
	index.upsert(embeddings)