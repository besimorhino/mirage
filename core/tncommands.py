#!/usr/bin/python

class Command():

    def __init__(self, word):
        self.word = word


    def commands(self, word):
        file1 = open('list.txt', 'r')
        fr = file1.read()
        for line in fr.splitlines():
            if self.word.lower() in line.lower():
                #print line
                return line