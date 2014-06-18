from django.contrib.auth.models import User, Group
from django.http import Http404

from artist.models import Artist
from event.models import Event

from rest_framework import authentication, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

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



class Artists(APIView):    
    """
    API endpoint for adding, and removing artist to users liked artists
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self, artist_name):
        """
        Helper method for retrieving artist
        """
        try:
            return Artist.objects.get(artist_name=artist_name)
        except Artist.DoesNotExist:
            raise Http404
    
    def get(self, request, artist_name, format=None):
        """
        API endpoint for getting artist data
        """
        artist = self.get_object(artist_name)
        serialized_artist = ArtistSerializer(artist)
        return Response(serialized_artist.data)
     
    def put(self, request, artist_name, format=None):
        """
        API endpoint for adding artist to users liked artists
        """
        artist = request.user.user.add_artist(artist_name)
        serialized_artist = ArtistSerializer(artist)
        if serialized_artist.is_valid():
            serialized_artist.save()
            return Response(serialized_artist.data)
        return Response(serialized_artist.errors, stats=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, artist_name, format=None):
        """
        API endpoint to remove artist from ccuser's liked artist
        """
        request.user.artists.remove_artist(artist_name)
        return Response(status=status.HTTP_204_NO_CONTENT)
        