
from django.contrib.auth.models import User, Group
from django.forms import widgets

from artists.models import Artist
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
    name = serializers.CharField(required=False, max_length=256)
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
            instance.name = attrs.get('name', instance.name)
            instance.bio = attrs.get('bio', instance.bio)
            instance.currently_touring = attrs.get('currently_touring', 
                                                   instance.currently_touring)
            instance.country_of_origin = attrs.get('country_of_origin', 
                                                   instance.country_of_origin)
            instance.genre = attrs.get('genre', instance.genre)
            return instance

        # Create new instance
        return Artist(**attrs)
    
