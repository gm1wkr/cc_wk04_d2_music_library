import pdb
from models.album import Album

from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.albums_repository as album_repository

artist_repository.delete_all()
album_repository.delete_all()


artist_1 = Artist("Queen")
artist_repository.save(artist_1)

artist_2 = Artist("Bob Dillan")
artist_repository.save(artist_2)

album_1 = Album("Its a kind of Magic", "Rock", artist_1)
album_repository.save(album_1)

# result = artist_repository.select(18)

pdb.set_trace()