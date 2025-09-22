from django.urls import re_path

from notes.consumers import NoteConsumer

websocket_urlpatterns = [
    re_path(r"ws/notes/$", NoteConsumer.as_asgi()),
    
]
