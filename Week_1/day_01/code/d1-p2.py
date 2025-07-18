import json
import pprint
with open("../input/dump-d1.json", "r") as file:
    data = json.load(file)

left = data["left"]
right = data["right"]
counter = {}
finalCounter = 0

for i in left:
    count = right.count(i)
    
    if count == 0:
        pass
    else:
        counter[i] = count

print(pprint.pprint(counter))

for key in counter:
    finalCounter += (int(key) * int(counter[key]))
    print(int(key),"*", int(counter[key]), "=", int(key) * int(counter[key]))
print(f"\n--=OUTPUT=--\nThe Final Distance = {finalCounter}\n")