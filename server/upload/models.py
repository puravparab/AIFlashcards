from django.db import models

class Document(models.Model):
	file = models.FileField(upload_to="uploads/")
	qa_json = models.JSONField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return (f'document #{self.id}')

class Text(models.Model):
	text = models.JSONField(null=False, blank=True)
	document = models.ForeignKey(Document, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return (f'Text #{self.id} - Doc #{self.document.id}')