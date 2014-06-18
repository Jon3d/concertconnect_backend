'''
Created on Jun 12, 2014

@author: jhuisingh
'''
from django.db import models
from django.contrib.auth.models import User
from artist.models import Artist
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class CCUser(models.Model):
    '''
    Model for extending normal django user
    '''
    user = models.ForeignKey(User, unique=True)
    liked_artists = models.ForeignKey(Artist, null=True, blank=True)

    def __init__(self, params):
        '''
        Constructor
        '''
        try:
            self.user = User.objects.create_user(username=params['username'], 
                                                 email=params['email'], 
                                                 password=params['password'])
            return self.user
        except KeyError:
            raise Exception("Attempted to create user without proper params")
        
    def add_artist(self, artist_name):
        '''
        add artist to users liked artist
        '''
        artist = Artist.retrieve_or_create_artist(artist_name)
        self.liked_artists.add(artist)
        logging.info('added artist %s from user %s', 
                     artist_name,
                     self.user.username)
        return artist
        
    def remove_artist(self, artist_name):
        '''
        Remove artist from liked artists
        '''
        try:
            artist = Artist.objects.get(artist_name=artist_name)
            self.liked_artists.remove(artist)
            logging.info('removed artist %s from user %s', 
                         artist_name,
                         self.user.username)
        except models.Model.DoesNotExist:
            logging.error('attempted to remove artist %s that does not exist',
                          artist_name)
            raise Exception('%s does not exist', artist_name)