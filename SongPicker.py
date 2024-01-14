import os
from random import randint
from random import shuffle

songs = []

def getSongs():
    rPath = os.getcwd() + '\\resources'
    print('Getting songs from ' + rPath + '.')
    songs = os.listdir(rPath)
    print(f'Got {len(songs)} songs.')
    shuffleSongs(songs)
    return songs

def shuffleSongs(songs):
    print('Shuffling...')
    shuffle(songs)
    print('Shuffled.')

def getSongPath(song):
    rPath = os.getcwd() + '\\resources'
    return rPath + '\\' + song

def nextSong(songs):
    print(f'Next Song: {songs[-1]}')
    nextSong = songs.pop()
    if (len(songs) <= 0):
        getSongs(songs)
        print('Reached')
    print(f'Up next: {songs[-1]}')
    return nextSong
