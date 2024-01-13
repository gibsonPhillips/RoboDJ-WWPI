
import SongPicker


def print_hi():
    #p = vlc.MediaPlayer("/resources\\Benjamin Lee - Sleeping (Lofi).mp3")

    #p.play()
    songs = SongPicker.getSongs()
    currentSong = SongPicker.pickSong(songs)
    print('Now playing: ' + currentSong)
    currentSongPath = SongPicker.getSongPath(currentSong)
    print('Song Path: ' + currentSongPath)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
