# Importing necessary modules and classes
import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# Deleting all records from the tables
artist_repository.delete_all()

# Creating and saving artist records
artist_1 = Artist("Michael", "Jackson")
artist_repository.save(artist_1)

artist_2 = Artist("The Beatles", "John, Paul, George, Ringo")
artist_repository.save(artist_2)

# Creating and saving album records
album = Album("Thriller", artist_1)
album_repository.save(album)

album_2 = Album("Abbey Road", artist_2)
album_repository.save(album_2)

# Retrieving all albums and artists
albums = album_repository.select_all()
artists = artist_repository.select_all()

# Setting up a debugger
pdb.set_trace()

# Deleting all records from the tables
# album_repository.delete_all()
