# 8-7, 8-8
# optional arguments with dictionary function


def make_album(artist, album_title, songs=None):
    album = {'Artist': artist, 'Album': album_title}
    if songs:
        album['Songs'] = songs
    return album


print(
    "***\nYou want to save info on your favorite albums\n"
    "so that you can look back in the future\n"
    "and see what you were listening to!\n***\n"
      )

while True:
    album = input("What is the name of this album? ")
    artist = input("Who is the artist? ")
    songs = int(input("How many songs are on the album?\n"
                      "If you aren't sure, type '0': "))
    print(f"\nCool! I've never heard of {artist.title()} before, but I'll do some research!"
          f"\nHere's the data I saved:\n")

    if songs == '0':
        album_data = make_album(artist, album)
    else:
        album_data = make_album(artist, album, songs)

    print(f"{album_data}\n")

    loop = input("Would you like to save another album? (yes/no): ")
    if loop == "yes":
        print("Let's do it!\n\n")
        pass
    else:
        print("That's enough for now. Bye!")
        break
