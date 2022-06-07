from db.run_sql import run_sql

from models.album import Album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        album = Album(
            row['title'],
            row['genre'],
            row['id']
        )
        albums.append(album)
    
    return albums


def selct(id):
    pass


def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id

    return album




def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)



def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)   

