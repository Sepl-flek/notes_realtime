import uuid

from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(default='', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    users = models.ManyToManyField(User, related_name='users')
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.pk}"
