
import SongPicker


def print_hi():
    #p = vlc.MediaPlayer("/resources\\Benjamin Lee - Sleeping (Lofi).mp3")

    #p.play()
    songs = SongPicker.getSongs()
    nextSong = SongPicker.nextSong(songs)
    print(nextSong)
    nextSongPath = SongPicker.getSongPath(nextSong)
    print(nextSongPath)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
