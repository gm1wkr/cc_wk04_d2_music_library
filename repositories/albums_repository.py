from unittest import result
from db.run_sql import run_sql

from models.album import Album
import repositories.artist_repository as artist_repository

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist_id = row['artist_id']
        artist = artist_repository.select(artist_id)
        album = Album(
            row['title'],
            row['genre'],
            artist
        )
        albums.append(album)
    
    return albums


def select(id):
    album = []
    sql = "SELECT * FROM albums WHERE id = '%s'"
    value = [id]
    result = run_sql(sql, value)[0]
    if result is not None:
        artist_id = row['artist_id']
        artist = artist_repository.select(artist_id)
        album = Album(
            result['title'],
            result['genre'],
            artist
        )
    return album




def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING id"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id

    return album


def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)



def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)   

