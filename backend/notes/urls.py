from rest_framework.routers import DefaultRouter, SimpleRouter

from notes.views import NoteViewSet

router = SimpleRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = router.urls
