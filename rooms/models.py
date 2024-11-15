from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from core.validators import validate_slug
import hashlib


# Create your models here.


import hashlib
from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    members = models.ManyToManyField(User)
    slug = models.SlugField(unique=True)
    is_private = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Get the user IDs and sort them to ensure consistent order
            user_ids = sorted([str(member.id) for member in self.members.all()])

            # Create a unique string from the sorted user IDs
            unique_string = "-".join(user_ids)

            # Hash the unique string using SHA-256 and truncate the result
            self.slug = hashlib.sha256(unique_string.encode("utf-8")).hexdigest()[:64]

        super().save(*args, **kwargs)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="message", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="message", on_delete=models.CASCADE)
    content = models.TextField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_at",)
