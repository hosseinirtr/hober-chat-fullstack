from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from core.validators import validate_slug

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=24)
    description = models.TextField(max_length=128)
    members = models.ManyToManyField(User)
    is_private = models.BooleanField(default=False)
    slug = models.SlugField(max_length=24, unique=True, validators=[validate_slug])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.is_private is True:
            self.slug = slugify(self.slug+"_gp")
        if not self.name:
            self.name = self.slug.replace("_", '').replace("-", '')
        if not self.slug:
            self.slug = slugify(self.name.replace(" ", '_'))
        if not self.slug and not self.name:
            raise ValidationError("Both 'name' and 'slug' cannot be empty.")
        super().save(*args, **kwargs)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="message", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="message", on_delete=models.CASCADE)
    content = models.TextField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at', )
