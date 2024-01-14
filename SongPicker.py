import os
from random import randint
from random import shuffle


class Songs:
    def __init__(self):
        self.pool = []
        self.rPath = ""
        self.getSongs()

    def getSongs(self):
        self.rPath = os.getcwd() + '\\resources'
        # print('Getting songs from ' + self.rPath + '.')
        self.pool = os.listdir(self.rPath)
        # print(f'Got {len(self.pool)} songs.')
        self.shuffleSongs()
        return self.pool

    def shuffleSongs(self):
        # print('Shuffling...')
        shuffle(self.pool)
        # print(self.pool)
        # print('Shuffled.')

    def getSongPath(self, song):
        return self.rPath + '\\' + song

    def nextSong(self):
        print(f'Current Song: {self.pool[-1]}')
        nextSong = self.pool.pop()
        if (len(self.pool) <= 0):
            self.getSongs()
            print('end of list - reshuffled')
        # print(self.pool)
        print(f'Up next: {self.pool[-1]}')
        return nextSong
