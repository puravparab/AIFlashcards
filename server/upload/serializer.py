from rest_framework import serializers
from .models import Document, Text

class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		fields = ('id', 'file', 'qa_json')

class TextSerializer(serializers.ModelSerializer):
	document = DocumentSerializer() 
	class Meta:
		model = Text
		fields = ('id', 'text', 'document')