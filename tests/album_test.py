# Importing necessary modules and classes for album tests
import unittest
from models.album import Album
from models.artist import Artist

class TestAlbum(unittest.TestCase):
    
    def setUp(self):
        artist = Artist("Michael", "Jackson")
        self.album = Album("Thriller", artist)
    
    def test_album_has_title(self):
        self.assertEqual("Thriller", self.album.title)
        
    def test_album_has_artist(self):
        self.assertEqual("Michael Jackson", self.album.artist.full_name)
