from db.run_sql import run_sql

from models.artist import Artist


def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    rows = run_sql(sql)
    for row in rows:
        artist = Artist(row['name'])
        artists.append(artist)

    return artists


def select(id):
    artist = None 
    sql = "SELECT * FROM artists WHERE id = '%s'"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result["name"], result['id'])

    return artist



def select_artist_by_name(artists_name):
    sql = "SELECT * FROM artists WHERE name = %s"
    values = [artists_name]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result['name'], result['id'])
    
    return artist


def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
    values = [artist.name]
    result = run_sql(sql, values)
    id = result[0]["id"]
    artist.id = id

    return artist

def update(artist, new_name):
    sql = "UPDATE artists SET name = %s WHERE id = %s"
    values = [new_name, artist.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)



def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)   