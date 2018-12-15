#
def make_album(singer_name, album_title, song_number=''):
    album = {'singer': singer_name.title(), 'album': album_title.title()}
    if song_number:
        album['songs'] = song_number
    return album

finished_album = make_album('mike', 'abcg',22)
print(finished_album)

#
def make_album(singer_name, album_title):
    album = {'singer': singer_name, 'album': album_title}
    return album

while True:
    s_name = input("Singer Name: ")
    if s_name == 'q':
        break
    A_name = input("Album Title: ")
    if A_name == 'q':
        break
    finished_album = make_album(s_name, A_name)
    print(finished_album)
