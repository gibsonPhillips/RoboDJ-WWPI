import os
from random import randint

def getSongs():
    rPath = os.getcwd() + '\\resources'
    songs = os.listdir(rPath)
    return songs

def getSongPath(song):
    rPath = os.getcwd() + '\\resources'
    return rPath + '\\' + song

def pickSong(songs):
    length = len(songs)
    num = randint(0,length-1)
    return songs[num]
