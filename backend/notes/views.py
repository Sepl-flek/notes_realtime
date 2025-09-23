from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet

from notes.models import Note
from notes.serializers import NoteSerializer


# Create your views here.

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all().prefetch_related('users')
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        note = serializer.save(owner=self.request.user)


class IndexView(TemplateView):
    template_name = "index.html"
