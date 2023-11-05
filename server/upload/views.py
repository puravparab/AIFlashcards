from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def upload_file(request, format=None):
	file = request.data.get("file")
	return Response({"text": file}, status=status.HTTP_200_OK)