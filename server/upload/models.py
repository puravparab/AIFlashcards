from django.db import models

class Document(models.Model):
	file = models.FileField(upload_to="uploads/")
	qa_json = models.JSONField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return (f'document #{self.id}')