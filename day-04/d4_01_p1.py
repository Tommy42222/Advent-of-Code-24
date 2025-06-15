import sys,os,re,time,pprint
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.homeGrownFunctions import openFile

def get_X(content):

    x_Match_list = [] # dict to store all matches and their coordinates
    pattern = re.compile('X') # search pattern
    matches = pattern.finditer(content) 

    for match in matches: 

        coordinate = int(match.start()) # get each matches coordinat and name (i.e., do()) and append them to the dict
        x_Match_list.append(coordinate)

    return(x_Match_list)


file = openFile("data4")

newfile = file.splitlines()


horizontal_Matches = file.count('XMAS') + file.count("SAMX")
print(f"Number of horizontal matches = {horizontal_Matches}")
number0fRows = file.count("\n") 
print(f"NUMBER OF ROWS = {number0fRows}")



xList = []
for row in range (number0fRows):
     xList.append(get_X(newfile[row]))

# print(xList)

for row in range(number0fRows-1):
    for item in range(len(xList[row])):
        print(f"Row_{row}:  {xList[row][item]}")
    
    print("---")

