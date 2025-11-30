def make_album(artist, title, n_songs=None):
    return {
        'artist_name': artist,
        'album_title': title,
        'number_songs': n_songs,
        }

#
print(make_album('scntfc', 'oxenfree'))

#
print(make_album('scntfc', 'oxenfree', '18'))

#
print(make_album('Yann van der Cruyssen', 'Stray - Original Soundtrack', '29'))

#
running = True

#
while running != 'quit':
    artist = input("\nEnter artist: ")
    title = input('Title: ')
    n_songs = input('Number of songs: ')

    #
    running = input('\nDo you wish to continue ("quit" to exit the program): ')

    #
    if running == quit:
        break



