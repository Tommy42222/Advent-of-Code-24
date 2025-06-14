import re


def getmul(content):



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

def openFile(fileName):
    with open(f"{fileName}", "r") as file: # opens file
        content = file.read()
        return content