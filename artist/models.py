from django.db import models
from django.db import transaction

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
    artist_name = models.CharField(max_length=256, blank=True, default='')
    artist_label = models.CharField(max_length=256, blank=True, default='')
    bio = models.TextField()
    currently_touring = models.BooleanField(default=False)
    country_of_origin = models.CharField(max_length=256, blank=True, default='')
    genre = models.CharField(max_length=256, blank=True, default='')
    events = models.ForeignKey(Event, null=True, blank=True)
    mbid = models.CharField(max_length=256, blank=True, default='')
    similar_artists = TaggableManager()
    
    class Meta:
        ordering = ('artist_name',)
    
    def __str__(self):
        return '%s' % self.artist_name
    
    def create_if_new(self, name):
        """
        Get existing or return new object
        """
        if not Artist.objects.filter(artist_name__iexact=name):
            Artist.objects.create(artist_name=name)
    
    @transaction.atomic
    def tag_similar(self):
        """
        Tags similar artists
        """
        if settings.LAST_FM_NETWORK and not self.similar_artists.all():
            requested_artist = settings.LAST_FM_NETWORK.get_artist(self.artist_name)
            #TODO: populate more info if needed
            artists = requested_artist.get_similar()
            for artist in artists:
                similar_artist_name = artist[0].name
                self.similar_artists.add(similar_artist_name)
                self.create_if_new(similar_artist_name)
                print(similar_artist_name)
                logger.debug("Added %s as similar artist to name %s",
                             similar_artist_name, 
                             requested_artist)
      
    def save(self, *args, **kwargs):
        """
        Override save to tag similar artists
        """ 
        super(Artist, self).save(*args, **kwargs)
        logger.info("Created a new Artist with the name %s", )
        
    @classmethod
    def create(cls, name):
        """
        Create's new artist object, and a new artist for each tagged artist
        if artist already exists, but not similarly tagged, tag similar
        """
        if not Artist.objects.filter(artist_name__iexact=name):
            artist = cls(artist_name=name)
            artist.save() 
            artist.tag_similar()
            logger.info("Created a new Artist, name %s", name)
            return artist
        else:
            artist = Artist.objects.get(artist_name__iexact=name)
            if not artist.similar_artists.all():
                artist.tag_similar()
            return artist
            
            
               
