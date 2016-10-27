"""
stomp.py
-----------
Utilities for working with stomp files

written for python 3.4 and up


tests are in test_stomp.py
"""

import os
import hashlib
from stomp import *
import re
import operator
import hashlib

def clean_lines(filename):
    #num_lines = 0
    with open(filename) as f:    
        for l in f:
            line = l.strip()
            if line:
                if not line.startswith('#'):
                    yield line
                    #print(line)
                    #num_lines += 1
                    #print(line)
    """ 1. with reading from the file at filename
        2. yield every line except:
           - lines that start with a "#" character
           - lines that are blank:while
           - lines that have empty space
    
    hint: you can do this in two lines.  Look at the itertools library
    """
    #raise NotImplementedError()

def get_cards_from_file(filename):
    """yield Card objects for every card in the stomp file 
    """
    cards = {}
    stop = '~'
    with open(filename) as f:
        li = f.readlines()
        for l in li:
            line = l.strip()
            if line:
                if not line.startswith('#'): #retrieving clean lines up to this point.
                    if line.startswith('~'):
                        #yield cards
                        title = line[1:]
                        start = title                                                                       
                        content = ""
                    if not line.startswith('~'):
                        content += l[l.find(start)+1 : l.find(stop)]
                        cards[title]=content                                                         
    #yield cards               
    print(cards)
    print(len(cards))    
        
    #raise NotImplementedError()

class Card:
    """ represents a Card in a STOMP input file """
    def __init__(self, name, options=[]):
        self.name = name
        self.options = options

    def add_option(self, raw_option):
        get_cards_from_file('test_files/input')
        print(cards[raw_option])
        """ add an option 
        
        raw_option is expected to be a string, read raw from the
        stomp input file.  The raw_option should be parsed
        and added to self.options
        
        """
        raise NotImplementedError()


def get_hash(filename, hashtype="sha512"):
    """ obtain a hash of the filename
    
    hashtype must be one of the hashes in the hashlib
        (note sha512 is a version of SHA-3)
    """
    with open(filename, 'br') as f:
        h = getattr(hashlib, hashtype)
        return h(f.read()).hexdigest()

class InputFile:
    """ represents a STOMP input file """
    def __init__(self, filename):
        """ given a filename, return an instance 
        
        """
        self.sha512_hash = get_hash(filename)
        """ a SHA-3 hash of the input file """
        self.cards = list(get_cards_from_file(filename))
        """ a list of Card objects, one for each card in the input file """

if __name__=="__main__":
    pass
