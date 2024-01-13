import vlc


def print_hi():
    p = vlc.MediaPlayer("/resources\\Benjamin Lee - Sleeping (Lofi).mp3")

    p.play()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
