import vlc
import SongPicker
import time
import os
os.add_dll_directory(os.getcwd())

def play_song(nextSongPath):
    # wack
    current_song = vlc.MediaPlayer(nextSongPath)
    current_song.play()
    time.sleep(1)
    duration = current_song.get_length()
    time.sleep((duration / 1000) - 2)

def main():
    #p = vlc.MediaPlayer("/resources\\Benjamin Lee - Sleeping (Lofi).mp3")

    #p.play()

    # instanciate variables for list of songs and current playing song
    sPicker = SongPicker.Songs()
    # current_song = ""


    while True:
        # just the title of the song
        nextSong = sPicker.nextSong()
        # print(nextSong)

        # just gets the path to the song
        nextSongPath = sPicker.getSongPath(nextSong)
        print(nextSongPath)
        play_song(nextSongPath)




def vlc_test():
    song = vlc.MediaPlayer("resources/Benjamin Lee - Sleeping (Lofi).mp3")
    song.play()
    time.sleep(1)
    duration = song.get_length()
    print(f"duration {duration}")
    # while True:
    #     duration = song.get_length()
    #     print(f"duration {duration / 1000}")
    #     time.sleep(1)
    #     duration -= 1.001
    time.sleep(duration / 1000)
    print("ah")


if __name__ == '__main__':
    main()

