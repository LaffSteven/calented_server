from django.db import models

# Create your models here.
class CalEvent(models.Model):
	date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	title = models.CharField(max_length=64)
	description = models.TextField(max_length=255)