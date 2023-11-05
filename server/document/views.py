from django.conf import settings
from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from upload.models import Document, Text
from upload.serializer import DocumentSerializer, TextSerializer

"""
View specific document
"""
@api_view(['GET'])
def get_document(request, id):
	document = Document.objects.get(id=id)
	serializer = DocumentSerializer(document)
	return Response({"data": serializer.data}, status=status.HTTP_200_OK)

"""
View all documents
"""
@api_view(['GET'])
def all_document(request):
	document = Document.objects.all()
	serializer = DocumentSerializer(document, many=True)
	return Response({"data": serializer.data}, status=status.HTTP_200_OK)