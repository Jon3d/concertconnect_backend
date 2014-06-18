
from django.contrib.auth.models import User, Group
from django.forms import widgets

from artist.models import Artist
from event.models import Event
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ArtistSerializer(serializers.Serializer):
    pk = serializers.Field()
    created = serializers.DateTimeField()
    artist_name = serializers.CharField(required=False, max_length=256)
    artist_label = serializers.CharField(required=False, max_length=256)
    bio = serializers.CharField(widget=widgets.Textarea,
                                max_length=100000)
    currently_touring = serializers.BooleanField(required=False)
    country_of_origin = serializers.CharField(required=False, max_length=256)
    genre = serializers.CharField(required=False, max_length=256)
    
    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.artist_name = attrs.get('name', instance.name)
            instance.artist_label = attrs.get('artist_label', instance.artist_label)
            instance.bio = attrs.get('bio', instance.bio)
            instance.currently_touring = attrs.get('currently_touring', 
                                                   instance.currently_touring)
            instance.country_of_origin = attrs.get('country_of_origin', 
                                                   instance.country_of_origin)
            instance.genre = attrs.get('genre', instance.genre)
            return instance

        # Create new instance
        return Artist(**attrs)
    
    
class EventSerializer(serializers.Serializer):
    pk = serializers.Field()
    created = serializers.DateTimeField()
    event_date = serializers.DateTimeField()
    
    event_name = serializers.CharField(required=False, max_length=256)
    event_description = serializers.CharField(widget=widgets.Textarea,
                                max_length=100000)
    venue_name = serializers.CharField(required=False, max_length=256)
    venue_address = serializers.CharField(required=False, max_length=256)
    venue_description = serializers.CharField(widget=widgets.Textarea,
                                max_length=100000)
    venue_phone_number = serializers.CharField(required=False, max_length=256)
    
    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.event_name = attrs.get('event_name', instance.event_name)
            instance.event_description = attrs.get('event_description',
                                                   instance.event_description)
            instance.venue_name = attrs.get('venue_name', instance.venue_name)
            instance.venue_address = attrs.get('venue_address',
                                               instance.venue_address)
            instance.venue_description = attrs.get('venue_description',
                                                   instance.venue_description)
            instance.venue_phone_number = attrs.get('venue_phone_number', 
                                                    instance.venue_phone_number)
            return instance

        # Create new instance
        return Event(**attrs)
    
