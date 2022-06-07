import pdb
from models.album import Album

from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.albums_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()


artist_1 = Artist("Queen")
artist_repository.save(artist_1)

artist_2 = Artist("Bob Dillan")
artist_repository.save(artist_2)

album_1 = Album("Its a kind of Magic", "Rock", artist_1)
album_repository.save(album_1)

album_2 = Album("Sheer Heart Attack", "Rock", artist_1)
album_repository.save(album_2)

album_3 = Album("News of the World", "Rock", artist_1)
album_repository.save(album_3)

# queen_id = artist_1.id
# res = artist_repository.select(queen_id)

artist_list = artist_repository.select_all()
album_list = album_repository.select_all()
is_queen = album_repository.select(album_list[2].id)

all_queen = album_repository.select_all_by_artist(artist_1)

bob = artist_repository.select_artist_by_name("Bob Dillan")
artist_repository.update(bob, "Bobby D")
bob_2 = artist_repository.select_artist_by_name("Bobby D")

pdb.set_trace()