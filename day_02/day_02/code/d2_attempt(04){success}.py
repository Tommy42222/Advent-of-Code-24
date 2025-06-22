
def checkRowDiff(row): # takes in a list of digits, iterates over the Nth, Nth + 1 pairs, if differnce between them are not between 1 and 3, return fail to program
    for item in range(len(row)-1):

        a,b = row[item],row[item+1] # gets Nth, Nth + 1 pair
        # print(a,b)
        diff = abs(a - b)

        if diff > 3 or diff <=0:
            return False
       
        else:
            continue

    return True # if no pairs diff are outside 1 to 3: then the row is safe


def getDirection(row): # takes in a list of digits, iterates over the Nth, Nth + 1 pairs, the first uneven pair desides the direction for the rest of the list
    for item in range(len(row)-1):
        a,b = row[item],row[item+1]

        if a > b: # e.g. 5,2
            return "decsend"
        
        elif a < b: # e.g. 1,4
            return "acsend"

        else:
            continue # if a and b are the same, keep iterating and checking  until a direction is found


def checkDirection(row,direction): #takes in a list of digits and a string, the directional string gathered from "getDirection" determines how the row is checked
    if direction == "acsend":
        if sorted(row) == row: # if a row is already in asending order, sorting the list will return the same value as the orginal
            return True
        
        else:
            return False
    
    elif direction == "decsend":
        if sorted(row,reverse=True) == row: # same logic as acsend, but with the sorted list reversed
            return True
        
        else:
            return False


def secondCheck(row): # takes in a list of digits, iterates over the list, creating a temp list with only the Nth digit removed, it then checks if that row is now safe, if yes, return TRUE to program
    original = row # saves original input

    for item in range(len(original)): 
        temp = original[:] # craete a soft copy
        temp.pop(item) # remove only the Nth item

        result = performChecks(temp) # function that performs the checks

        if result == True: 
            print(f"{original} can be made safe >>> {temp}\n")
            return True
        

def performChecks(newRow): # takes in a list of digits, calls 3 functions, and if the row is safe, returns TRUE to the program

    is_Diff_Safe = checkRowDiff(newRow) 
    get_Direction = getDirection(newRow) 
    is_Direction_Safe = checkDirection(newRow,get_Direction)


    if is_Diff_Safe and is_Direction_Safe == True:
        return True
    else:
        return False



with open("../input/data2.txt", "r") as file:  # opens the data.txt file
    content = file.read()

formatedList = [] # container for the parsed data

safeCount = 0 # counts the number of safe and unsafe rows
failCount = 0


splitConent = content.splitlines() # parses the data
for numbs in splitConent: 
    formatedList.append(numbs.split(" "))

dataList = [list(map(int, i)) for i in formatedList]


for row in range(len(dataList)): # for row in data2.txt, 

    currentRow = dataList[row] # gets the Nth row    
    

    is_Row_Safe = performChecks(currentRow) # checks if the row is safe


    if is_Row_Safe == True: 
        print(f"{row} {dataList[row]} = SAFE")
        safeCount += 1

    else:
        print(f"{row} {dataList[row]} == FAIL")

        output = secondCheck(currentRow) # if the row is not safe, check if it can be made safe by removing a single item from the row

        if output == True: # if removing a single digit can make the row safe, increament the safe counter, otherwise the row is not safe
            safeCount += 1

        else:
            failCount += 1

        

print(safeCount, failCount) # prints the final count of safe and unsafe rows