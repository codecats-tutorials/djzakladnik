from django.db import models
from django.contrib import auth

class Details(models.Model):
    user = models.OneToOneField(auth.models.User)

class Bookmarks(models.Model):
    title = models.CharField(max_length = 255)
    url = models.CharField(max_length = 255)
    description = models.TextField()
    author = models.ForeignKey(Details, related_name = 'author')
    subscribers = models.ManyToManyField(Details, related_name = 'subscribers')