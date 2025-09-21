from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from notes.models import Note
from notes.serializers import NoteSerializer


# Create your views here.

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all().prefetch_related('users')
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
