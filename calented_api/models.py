from turtle import title
from django.db import models

# Create your models here.
class CalEvent(models.Model):
	title = models.CharField(max_length=64)
	description = models.TextField(max_length=255)