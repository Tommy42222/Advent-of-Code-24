
def checkDiff(row):
    for item in range(len(row)-1):
        a,b = row[item],row[item+1]
        # print(a,b)

        diff = abs(a - b)

        if diff > 3 or diff <=0:
            return False
        else:
            continue

    return True # if no pairs diff are outside 1 to 3: then the row is safe

def getDirection(row):
    for item in range(len(row)-1):
        a,b = row[item],row[item+1]

        if a > b:
            return "decsend"
        
        elif a < b:
            return "acsend"
        
        else:
            continue # if a and b are the same, keep iterating and checking for until a direction is found




def checkDirection(row,direction):
    if direction == "acsend":
        if sorted(row) == row:
            return True
        
        else:
            return False
    
    elif direction == "decsend":
        if sorted(row,reverse=True) == row:
            return True
        
        else:
            return False


def secondCheck(row):
    original = row

    for item in range(len(original)):
        temp = original[:]
        temp.pop(item)


        result = performSecondCheck(temp)

        if result == True:
            print(f"{original} can be safe >>> {temp}")
            return True
        
def performSecondCheck(newRow):

    direction = getDirection(newRow)

    outputDiff = checkDiff(newRow)

    outputDirection = checkDirection(newRow,direction)


    if outputDiff and outputDirection == True:
        return True
    else:
        return None



with open("data2.txt", "r") as file:  # opens file
    content = file.read()

formatedList = []
safeCount = 0
failCount = 0
splitConent = content.splitlines()

for numbs in splitConent:
    formatedList.append(numbs.split(" "))

dataList = [list(map(int, i)) for i in formatedList]


for row in range(len(dataList)):

    currentRow = dataList[row]

    direction = getDirection(currentRow)

    outputDiff = checkDiff(currentRow)

    outputDirection = checkDirection(currentRow,direction)

    # print(f"{dataList[row]}| DIRECTION = {direction}| DIFF = {outputDiff}| CONSIST = {outputDirection}")

    if outputDiff == True and outputDirection == True:
        print(f"{row} {dataList[row]} = SAFE")
        safeCount += 1

    else:
        print(f"{row} {dataList[row]} == FAIL")

        output = secondCheck(currentRow)

        if output == True:
            safeCount += 1

        else:
            failCount += 1

        

print(safeCount, failCount)