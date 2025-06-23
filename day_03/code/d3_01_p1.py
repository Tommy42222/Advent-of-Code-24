import re
# mul(2,4)



def getmul(content):



    finalSum = 0

    pattern = re.compile('mul\(\d+,\d+\)')
    firstMatches = pattern.findall(content)

    for match in firstMatches:
        

        pattern1 = re.compile("\d+")
        firstPair = pattern1.search(match)
        

        pattern2 =re.compile(",\d+")
        secondPair = pattern2.search(match)

        x = secondPair.group()
        secondPair = x[1:]
        multProdoct = int(firstPair.group()) * int(secondPair)

        print(f"{firstPair.group()} * {secondPair} = {int(firstPair.group()) * int(secondPair)}")
        print(f"{finalSum} + {multProdoct} = {finalSum + multProdoct}\n")
        finalSum += multProdoct
    return finalSum


def openFile(fileName):
    with open(f"{fileName}", "r") as file: # opens file
        content = file.read()
        return content
    
if __name__ == "__main__":

    content = openFile("../input/input3.txt")
    finalsumm = getmul(content)    
    print(f"FINAL_TOTAL = {finalsumm}\n")



