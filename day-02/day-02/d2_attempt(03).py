import time

def getDifference(a,b):
     diff = abs(a - b)
     return diff

def getDirection(row):

    for item in range(len(dataList[row]) - 1):
        a, b = dataList[row][item], dataList[row][item + 1]
        
        if a == b:
             continue
        
        elif a > b:
            return "decsend"
            
        elif a < b:
            return "ascend"
        
   
def checkDirection(a,b,direction):
    if a == b:
        return "fail"
    
    elif direction == "ascend":
        if a > b:
            return "fail"
        else:
            return "safe"
    
    elif direction == "decsend":
        if a < b:
            return "fail"
        else:
            return "safe"
    
  
        


def checkDiff(diff):
    if diff > 3 or diff <= 0:
        return "fail"
    else:
         return "safe"


def secondCheck(row,direction):
    original = row
    
    print(f'OG == {original}')

    for item in range(0,len(original)):
        temp = original[:]
        temp.pop(item)
        

        # print(f"TEMP == {temp}")
        outputList = []
        for item in range(len(temp)-1) :
            
            
            a,b = temp[item], temp[item + 1]
            # print(a,b)
            diff = getDifference(a,b)
            output = checkDiff(diff) + checkDirection(a,b,direction)
            
    

            outputList.append(output)
            x = "".join(outputList)
       

        if "fail" in x:
            # print(f"ROW {temp} == FAIL")
            pass

        else:
            print(f"ROW {temp} inside of {original} == SAFE")

        
        # print(f"OUTPUT = {outputList}")
        # print("\n")
        
        outputList = []
           

       

        



with open("data2.txt", "r") as file:  # opens file
    content = file.read()


safeCount = 0
notSafeCount = 0
outputList = []
formatedList = []
splitConent = content.splitlines()  #
for numbs in splitConent:
    formatedList.append(numbs.split(" "))

dataList = [list(map(int, i)) for i in formatedList]


for row in range(1000):

    direction = getDirection(row)
    



    for item in range(len(dataList[row]) - 1):
        a, b = dataList[row][item], dataList[row][item + 1]
        
        diff = getDifference(a,b)
        output = checkDiff(diff) + checkDirection(a,b,direction)
        

        if "fail" in output:
            currentRow = dataList[row]
            notSafeCount += 1
            sc = secondCheck(currentRow,direction)

            if sc == "safe":
                print(f"{row} can be safe")
            break
            
                
      

            
                
            
            
        
        
    else:
        # print(row, "safe")
        safeCount += 1
    

print(safeCount,notSafeCount)
        
            
            
            
            



