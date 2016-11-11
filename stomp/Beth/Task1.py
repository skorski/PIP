"""
Task1.py
-----------
Utilities for retrieving stomp model runs on \\green and \\olive

written for python 3.4 and up


tests are in test_stomp.py
"""
import os
import xlwt
import csv

filepaths = []

def find_file(name, path): #name is filename, path is drive
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def find_stomp_runs_Z():
    
    stomp_runs_Z = []
    
    filepath = find_file('output', 'Z:\\')
    stomp_runs_Z.append(filepath)
    
    return stomp_runs_Z
    
                
def find_stomp_runs_X():

    stomp_runs_X = []
    
    filepath = find_file('output', 'X:\\')
    stomp_runs_X.append(filepath)
    return stomp_runs_X
    
def excel_export():
    olive_excel = find_stomp_runs_Z()
    #oe = ", ".join(map(str, olive_excel))
    result = open("olive_stomp.csv", 'w')
    writer = csv.writer(result)
    writer.writerows(olive_excel)
    result.close()
    
    


            
                
    
    
        
if __name__=="__main__":
    pass