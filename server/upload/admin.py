from django.contrib import admin

from .models import Document

@admin.register(Document)
class Document(admin.ModelAdmin):
	list_display = ('id', 'file', 'created_at')
	fields = ['file', 'qa_json']

	# search_fields = ('image', 'time', 'status')