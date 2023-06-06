# Importing necessary modules and classes for artist tests
import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    
    def setUp(self):
        self.artist = Artist("Michael", "Jackson")
    
    def test_artist_has_first_name(self):
        self.assertEqual("Michael", self.artist.first_name)
        
    def test_artist_has_last_name(self):
        self.assertEqual("Jackson", self.artist.last_name)
