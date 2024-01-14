import vlc
import SongPicker
import time
import random
import os
# os.add_dll_directory(os.getcwd())

def play_song(nextSongPath):
    current_song = vlc.MediaPlayer(nextSongPath)
    current_song.play()
    time.sleep(1)   # necessary for the duration to be filled with real number
    duration = current_song.get_length()    # length in miliseconds
    time.sleep((duration / 1000) - 2)


def get_rand_tag():

    # grab current working directory along with the path to tags (refactors easily)
    temp_path = os.getcwd() + '\\resources\\tags\\Rock'


    # use tempPath to create a list of available tags
    tag_list = os.listdir(temp_path)

    # select a random tag from tag_list
    tag_path = f"{temp_path}\\{random.choice(tag_list)}"
    print(tag_path)
    return tag_path



def play_tag():
    tag_file = get_rand_tag()
    tag = vlc.MediaPlayer(tag_file)
    tag.play()
    time.sleep(3)
    duration = tag.get_length()
    print(duration)
    time.sleep((duration / 1000) - 1)


def main():
    #p = vlc.MediaPlayer("/resources\\Benjamin Lee - Sleeping (Lofi).mp3")

    #p.play()

    # instanciate variables for list of songs and iterator
    sPicker = SongPicker.Songs()
    iterator = 0

    while True:
        # just the title of the song
        nextSong = sPicker.nextSong()
        # print(nextSong)

        # just gets the path to the song
        nextSongPath = sPicker.getSongPath(nextSong)
        print(nextSongPath)

        # calls helper function
        play_song(nextSongPath)

        # calls helper function every other time
        if (iterator % 2 == 0):
            play_tag()




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

