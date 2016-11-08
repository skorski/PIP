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
        list_nv = []
        list_nv = line.split(",")
        #print(list_nv)
        name = list_nv[0]
        #print(name)
        
        values = list_nv[1:] 
        #print(values)
        return Option(name, values)

        
    def get_option(self):
        return "\n".join([self.name, ", ".join(map(str, self.values))])
    
    def __str__(self):
            return Option.get_option(self) 
    
    def add_value(self, value):
        """Placeholder for what will go here"""
    
        raise NotImplementedError()    
        
def get_cards_from_file(filename):
    """yield Card objects for every card in the stomp file 
    """
    options = []
    title = ""
    
    for l in clean_lines(filename):
        if l.startswith('~'):
            if options != []:
                card = Card(title, options)
                yield card
            title = l                
            options = []
        else:
            o = Option.option_from_string(l)
            options.append(o)
            
                
    yield card    
        
    #raise NotImplementedError()

        
class Card:
    """ represents a Card in a STOMP input file """
    def __init__(self, title, options=[]):
        self.title = title[1:]
        self.options = options
          
        
    def card_report(self):
        return  "\n".join([self.title, ", ".join(map(str, self.options))])
    
    def get_report(card):
        return card.card_report()
        
    def __str__(self):
      return self.title
        
        
    @classmethod
    def add_option(self, raw_option):
    
    
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
