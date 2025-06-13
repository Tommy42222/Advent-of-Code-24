import json
# with open("data1.txt", "r") as file: # opens file
#     content = file.read()


# left = [] #holds all data on the left
# right = []

# data = content.splitlines()



# for row in data:
#     a,b = row.split()
#     left.append(a)
#     right.append(b)







# open("dump.json", 'w').write(json.dumps({"left":left,"right":right}))

with open("dump-d1.json", "r") as file:
    data = json.load(file)

left = data["left"]
right = data["right"]
totalDistance = []





for item in range(len(left)):
    totalDistance.append(abs(int(left[item]) - int(right[item])))
    print(f"Row -{item}- {left[item]} - {right[item]} = {totalDistance[item]}")
finalSum = sum(totalDistance)

print(f"Final_Total_Distance_is_{finalSum}")