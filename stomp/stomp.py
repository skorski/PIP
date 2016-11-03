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
from itertools import dropwhile
from itertools import filterfalse
from itertools import takewhile


def clean_lines(filename):  
    with open(filename) as f:    
        d = list(filterfalse(lambda l: l.strip() == "" or l.startswith('#'), f))            
    return d
    
                    
    """ 1. with reading from the file at filename
        2. yield every line except:
           - lines that start with a "#" character
           - lines that are blank:while
           - lines that have empty space
    
    hint: you can do this in two lines.  Look at the itertools library
    """
    #raise NotImplementedError()

class Option:
    def __init__(self, name, values=[]):
        self.name = name
        self.values = values
        
    @classmethod 
    def option_from_string(cls, line):
        list_nv = line.split(",")
        name = list_nv[0]
        values = list_nv[1:-1]
         
        return Option(name, values)
    
    def __str__(self):
        v = str(self.values)
        
        return self.name
    
    def add_value(self, value):
        """Placeholder for what will go here"""
    
        raise NotImplementedError()    
        
def get_cards_from_file(filename):
    """yield Card objects for every card in the stomp file 
    """
    options = []
    name = ""
    values = []
    
    for l in clean_lines(filename):
        if l.startswith('~'):
            if options != []:
                card = Card(l, options)
                yield card
                
            title = l[1:]
        else:
            Option.option_from_string(l)
            options.append(Option(name, values))
    
    yield card   
        
    #raise NotImplementedError()
    
class Card:
    """ represents a Card in a STOMP input file """
    def __init__(self, title, options=[]):
        self.title = title[1:]
        self.options = options
        
    def __str__(self):
        o = str(self.options)
        #c = "\n".join([self.title]) ",".join([o]))
        return self.title + o
        
        
    @classmethod
    def add_option(self, raw_option):
    
    
        raise NotImplementedError()
        
def see_card_objects(filename):
    for card in get_cards_from_file(filename):
        print(card) 

def see_option_objects(filename):
    for options in get_cards_from_file(filename):
        print(options)


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
