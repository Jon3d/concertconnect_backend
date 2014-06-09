from django.db import models
from event.models import Event

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
    events = models.ForeignKey(Event)
    
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return '%s' % self.name