from django.contrib.auth.models import User, Group
from rest_framework.serializers import HyperlinkedModelSerializer
from api.models import Note


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class NoteSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
