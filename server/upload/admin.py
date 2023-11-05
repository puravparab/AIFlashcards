from django.contrib import admin

from .models import Document, Text

@admin.register(Document)
class Document(admin.ModelAdmin):
	list_display = ('id', 'file', 'created_at')
	fields = ['file', 'qa_json']

	# search_fields = ('image', 'time', 'status')

@admin.register(Text)
class Text(admin.ModelAdmin):
	list_display = ('id', 'text', 'document', 'created_at')
	fields = ['text', 'document']