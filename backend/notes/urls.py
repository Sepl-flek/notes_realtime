from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from notes.views import NoteViewSet, IndexView

router = SimpleRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
urlpatterns += router.urls
