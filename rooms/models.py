from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="message", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="message", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at', )
