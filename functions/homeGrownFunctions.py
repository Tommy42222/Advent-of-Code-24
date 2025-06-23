# This file contains a list of functions that can be imported to other files in the "AOC24" directory.
import re


def getmul(content): # function for day 3, searches input text with regex for "mul(xxx,yyy) mults x*y, then sums and return the results".



    finalSum = 0

    pattern = re.compile('mul\(\d+,\d+\)')
    firstMatches = pattern.findall(content)

    for match in firstMatches:
        print(match)

        pattern1 = re.compile("\d+")
        firstPair = pattern1.search(match)
        

        pattern2 =re.compile(",\d+")
        secondPair = pattern2.search(match)

        x = secondPair.group()
        secondPair = x[1:]
        multProdoct = int(firstPair.group()) * int(secondPair)

        print(f"{finalSum} + {multProdoct} = {finalSum + multProdoct}\n")
        finalSum += multProdoct
    return finalSum

def openFile(fileName): # takes in a file name, opens it, and returns the file as a string.
    with open(f"input/{fileName}.txt", "r") as file: 
        content = file.read()
        return content
    
