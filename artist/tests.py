from django.test import TestCase
import nose
import mock

from artist.models import Artist

class Test(TestCase):

    def setUp(self):
        self.name = 'test_artist'
        self.genre = 'test'
        self.artist = Artist.objects.create(artist_name=self.artist_name,
                                            genre=self.genre)

    def tearDown(self):
        Artist.objects.all().delete()

    def test_create_if_new_new(self):
        artist = Artist.objects.create(artist_name='new_artist', 
                                       genre='test_rock')
        assert artist.pk != self.artist.pk, (artist.pk, self.artist.pk)
    
    def test_create_if_new_not_new(self):
        artist = Artist.objects.create(name=self.name,
                                       genre=self.genre)
        assert artist.pk == self.artist.pk, (artist.pk, self.artist.pk)
