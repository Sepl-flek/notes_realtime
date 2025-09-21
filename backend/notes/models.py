import uuid

from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    edit_key = models.UUIDField(default=uuid.uuid4, unique=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.edit_key}"
