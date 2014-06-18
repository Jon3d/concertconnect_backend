from django.db import models
from django.db import transaction
from django.contrib.auth.models import User

from django.conf import settings

from event.models import Event

import logging

from taggit.managers import TaggableManager

# Get an instance of a logger
logger = logging.getLogger(__name__)

class Artist(models.Model):
    '''
    Artist model for artist information, TODO: Add picture functionality
    '''        
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=256, blank=True, default='')
    artist_label = models.CharField(max_length=256, blank=True, default='')
    bio = models.TextField()
    currently_touring = models.BooleanField(default=False)
    country_of_origin = models.CharField(max_length=256, blank=True, default='')
    genre = models.CharField(max_length=256, blank=True, default='')
    mbid = models.CharField(max_length=256, blank=True, default='')
    similar_artists = TaggableManager()
    
    events = models.ForeignKey(Event, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    
    class Meta:
        unique_together= (('name', 'genre'),)
        ordering = ('name',)

    def __str__(self):
        return '%s' % self.artist_name

    def create_if_new(self, name):
        '''
        Get existing or return new object
        '''
        if not Artist.objects.filter(name__iexact=name):
            Artist.objects.create(name=name)

    @transaction.atomic 
    def get_last_fm_artist(self):
        '''
        Gets artist object from last fm network
        TODO add locks based on artist name, not global
        '''
        return settings.LAST_FM_NETWORK.get_artist(self.name)
        
    @transaction.atomic
    def get_similar_artists_from_last_fm(self, last_fm_artist):
        '''
        Gets similar artists from a last_fm artist object
        '''
        similar_artists = last_fm_artist.get_similar()
        return similar_artists   
        
    @transaction.atomic
    def tag_similar(self, similar_artists):
        '''
        Tags similar artists
        '''
        for artist in similar_artists:
            if artist not in self.similar_artists.all():
                similar_artist_name = artist[0].name
                self.similar_artists.add(similar_artist_name)
                self.create_if_new(similar_artist_name)
                logger.debug("Added %s as similar artist to name %s",
                             similar_artist_name, 
                             self.artist_name)

    def retrieve_or_create_artist(self, artist_name):
        '''
        Retrieve's artist object, if it exists. if not, creates ccuser
        and tags similar artists
        '''
        if not Artist.objects.filter(name__iexact=artist_name):
            artist = Artist.objects.create(name=artist_name)
            artist.save() 
            artist.tag_similar()
            logger.info("Created a new Artist, name %s", artist_name)
            return artist
        else:
            artist = Artist.objects.get(name__iexact=artist_name)
            if not artist.similar_artists.all():
                artist.tag_similar()
            return artist