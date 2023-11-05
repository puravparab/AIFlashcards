from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Document

@api_view(['POST'])
def upload_file(request, format=None):
	file = request.data.get("file")
	return Response({"text": file}, status=status.HTTP_200_OK)

def create_document_entry(file):
	try:
		request = Document.objects.create(
			file = file,
			qa_json = {},
		)
		request.save()
		return request.id
	except:
		return None