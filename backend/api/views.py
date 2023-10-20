from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets
from api.models import Note
from api.serializers import (
    UserSerializer,
    GroupSerializer,
    NoteSerializer,
)


routes = [
    {
        'Endpoint': '/notes/',
        'method': 'GET',
        'body': None,
        'description': 'Return an array of notes'
    },
    {
        'Endpoint': '/notes/id',
        'method': 'GET',
        'body': None,
        'description': 'Return a single note object'
    },
    {
        'Endpoint': '/notes/create/',
        'method': 'POST',
        'body': {'body': ""},
        'description': 'Create a new note'
    },
    {
        'Endpoint': '/notes/id/update/',
        'method': 'PUT',
        'body': {'body': ""},
        'description': 'Update an existing note'
    },
    {
        'Endpoint': '/notes/id/delete/',
        'method': 'DELETE',
        'body': None,
        'description': 'Delete an exiting note'
    },
]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
