"""
Task1.py
-----------
Utilities for retrieving stomp model runs on \\green and \\olive

written for python 3.4 and up


tests are in test_stomp.py
"""
import os

target = "output"
folder = "working_data"

def find_file(target, folder): #target will be filename, folder I am hoping can be working_data.
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        if os.path.isdir(path):
            result = find_file(target, path)
            if result is not None:
                return result
            continue
        if f == target:
            return path

def find_stomp_runs():
    
    drives = ['Z:\\', 'X:\\']

    for drive in drives:
        if os.path.isdir(drive):
            filepath = find_file('output', drive)
            return filepath
            if filepath is not None:
                break
            
        
if __name__=="__main__":
    pass