# Importing necessary modules and classes
import pdb
from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

# Function to retrieve all albums
def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row["artist_id"])
        album = Album(
            row["title"],
            artist,
            row["id"],
        )
        albums.append(album)
    return albums

# Function to retrieve an album by ID
def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result["artist_id"])
        album = Album(
            result["title"],
            artist,
            result["id"],
        )
    return album

# Function to save an album
def save(album):
    sql = "INSERT INTO albums (title, artist_id) VALUES (%s, %s) RETURNING *"
    values = [album.title, album.artist.id]
    result = run_sql(sql, values)
    id = result[0]["id"]
    album.id = id

# Function to delete all albums
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

# Function to delete an album by ID
def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Function to update an album
def update(album):
    sql = "UPDATE albums SET (title, artist_id) = (%s, %s) WHERE id = %s"
    values = [album.title, album.artist.id, album.id]
    run_sql(sql, values)
