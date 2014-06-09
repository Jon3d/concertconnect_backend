from django.db import models

# Create your models here.
class Event(models.Model):
    '''
    Event model for event information, TODO: Add photo functionality
    '''
    created = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField(blank=True)
    event_name = models.CharField(max_length=256, blank=True, default='')
    event_description = models.TextField()
    venue_name = models.CharField(max_length=256, blank=True, default='')
    venue_address = models.CharField(max_length=256, blank=True, default='')
    venue_description = models.TextField()
    venue_phone_number = models.CharField(max_length=256, blank=True, default='')
    genre = models.CharField(max_length=256, blank=True, default='')
    

    class Meta:
        ordering = ('created',)
        
    def __str__(self):
        return '%s, %s' % (self.event_name, self.venue_name)