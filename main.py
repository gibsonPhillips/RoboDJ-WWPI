import vlc
import SongPicker
import time
import os
os.add_dll_directory(os.getcwd())

def main():
    #p = vlc.MediaPlayer("/resources\\Benjamin Lee - Sleeping (Lofi).mp3")

    #p.play()

    sPicker = SongPicker.Songs()

    while True:
        # just the title of the song
        nextSong = sPicker.nextSong()
        # print(nextSong)

        # just gets the path to the song
        nextSongPath = sPicker.getSongPath(nextSong)
        print(nextSongPath)

        # wack
        time.sleep(3)

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

