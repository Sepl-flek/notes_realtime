import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from notes.models import Note
from notes.serializers import NoteSerializer


class NoteApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.note1 = Note.objects.create(name='Note1', content='123', owner=self.user, public=True)
        self.note2 = Note.objects.create(name='Note2', content='123', owner=self.user, public=True)

    def test_get(self):
        url = reverse('note-list')
        notes = Note.objects.all().prefetch_related('users')

        response = self.client.get(url)
        serializer_data = NoteSerializer(notes, many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_one(self):
        url = reverse('note-detail', args=(self.note1.id,))

        response = self.client.get(url)
        notes = Note.objects.all().prefetch_related('users').first()
        serializer_data = NoteSerializer(notes).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        url = reverse('note-list')
        data = {'name': 'Note3', 'public': False, 'content': ''}

        self.client.force_login(self.user)
        response = self.client.post(url, data, format='json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Note.objects.count())
        self.assertEqual(self.user, Note.objects.last().owner)

