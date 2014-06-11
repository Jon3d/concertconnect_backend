from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from artist.models import Artist
from event.models import Event
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, EventSerializer, ArtistSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    
class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
# @api_view(['GET'])
# def get_similar(request, artist):
#     """
#     List all similar artists.
#     """
#     if request.method == 'GET':
#         if Artist.objects.filter(name=artist):
#             artist = Artist.objects.get(name=artist)
#         else:
#             artist = Artist.objects.create(name=artist)
#         serializer = ArtistSerializer()
#         return Response(serializer.data)