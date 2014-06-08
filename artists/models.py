from django.db import models

class Artist(models.Model):
    '''
    Artist model for artist information, TODO: Add picture functionality
    '''
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=256, blank=True, default='')
    bio = models.TextField()
    currently_touring = models.BooleanField(default=False)
    country_of_origin = models.CharField(max_length=256, blank=True, default='')
    genre = models.CharField(max_length=256, blank=True, default='')
    

    class Meta:
        ordering = ('created',)
