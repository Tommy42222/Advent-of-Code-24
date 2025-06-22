
import time

userInput = input("How many fails are allowed?\n>>> ")


with open("../input/data2.txt", "r") as file:  # opens file
    content = file.read()


def ac(f, s):
    if f < s:
        return 1
    else:
        return 0


def d(f, s):
    if f > s:
        return 1
    else:
        return 0


safeListCounter = 0  # total number of safe tests
formatedList = []  # list the formated content goes in
differnce = 0
sumFailCounter = []


splitConent = content.splitlines()  #
for numbs in splitConent:
    formatedList.append(numbs.split(" "))

dataList = [list(map(int, i)) for i in formatedList]
print("test")

for row in range(len(dataList)):
    iterationCounter = 0
    direction = ""
    fail_counter = 0
    fail_list = []
    for item in range(len(dataList[row]) - 1):

        a, b = dataList[row][item], dataList[row][item + 1]

        # only run this block on the first check of each row
        # if a > b: then track desending: else track ascending

        # if diff between a and b is greater then 3 and less then or equile to 0: break

        differnce = abs(a - b)
        if differnce > 3 or differnce <= 0:
            fail_counter += 1
            fail_list.append("DIFF")

        if direction == "":
            if a > b:
                direction = -1
            elif a < b:
                direction = 1
            else:
                continue

        elif direction == -1:
            output = d(a, b)
            if output == 0:

                fail_list.append("D")
                fail_counter += 1

        else:
            output = ac(a, b)
            if output == 0:
   
                fail_list.append("A")
                fail_counter += 1


    if fail_counter == int(userInput):
        
        print(f"{dataList[row]} is GOOD: {fail_counter} {fail_list}")
        safeListCounter += 1

    else:
        print(f"{dataList[row]} is BAD: {fail_counter} {fail_list}")

print(safeListCounter)
