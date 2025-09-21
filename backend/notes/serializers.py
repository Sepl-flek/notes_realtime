from rest_framework.serializers import ModelSerializer

from notes.models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        extra_kwargs = {
            'owner': {'read_only': True},
            'users': {'required': False},
            'content': {'required': False, 'allow_blank': True}
        }
