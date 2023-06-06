# Importing necessary modules and classes
import pdb
from db.run_sql import run_sql
from models.artist import Artist

# Function to retrieve all artists
def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(
            row["first_name"],
            row["last_name"],
            row["id"],
        )
        artists.append(artist)
    return artists

# Function to retrieve an artist by ID
def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(
            result["first_name"],
            result["last_name"],
            result["id"],
        )
    return artist

# Function to save an artist
def save(artist):
    sql = "INSERT INTO artists (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [artist.first_name, artist.last_name]
    result = run_sql(sql, values)
    id = result[0]["id"]
    artist.id = id

# Function to delete all artists
def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

# Function to delete an artist by ID
def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Function to update an artist
def update(artist):
    sql = "UPDATE artists SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [artist.first_name, artist.last_name, artist.id]
    run_sql(sql, values)
