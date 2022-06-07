from db.run_sql import run_sql

from models.artist import Artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    rows = run_sql(sql)
    for row in rows:
        artist = Artist(row['artist'])
        artists.append(artist)

    return artists