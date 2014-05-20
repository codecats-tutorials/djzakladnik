from django.db import models
from django.contrib import auth

class Profile(models.Model):
    user = models.OneToOneField(auth.models.User)

class Bookmark(models.Model):
    title = models.CharField(max_length = 255)
    url = models.CharField(max_length = 255)
    description = models.TextField()
    author = models.ForeignKey(Profile)
    subscribers = models.ManyToManyField(Profile, related_name = 'subscribers+')