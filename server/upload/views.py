from django.conf import settings
from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import openai
from openai.embeddings_utils import get_embedding
openai.api_key = settings.OPEN_AI

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
		# Access the file's content
		file_content = file.read().decode('utf-8')
		# Now, you can process the 'file_content' as a text string
		count = 0
		for line in file_content.split('\n'):
			if count > 10:
				break

			if line != "\r":
				# embedding = create_embedding(line)
				print(line)
				text_id = create_text_entry(line, f_id)
				# print(embedding)
				count += 1
		return Response({"file_id": f_id}, status=status.HTTP_200_OK)

	return Response({"error": "error creating document entry"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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