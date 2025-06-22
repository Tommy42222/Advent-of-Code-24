import re,pprint
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.homeGrownFunctions import getmul

def openFile(fileName):
    with open(f"{fileName}.txt", "r") as file: # opens file
        content = file.read()
        return content



def get_do(content):

    do_Match_dict = {} # dict to store all matches and their coordinates
    pattern = re.compile('do\(\)') # search pattern
    matches = pattern.finditer(content) 

    for match in matches: 

        coordinate = int(match.end()) # get each matches coordinate and title (i.e., do()) and append them to the dict
        title = str(match.group()) 
        do_Match_dict[coordinate] = title

    return(do_Match_dict)




def get_dont(content,dont_Matches_Dict):

    pattern = re.compile('don\'t\(\)') # search pattern
    matches = pattern.finditer(content) 

    for match in matches: 

        coordinate = int(match.end()) # get each matches coordinat and name (i.e., don't()) and append them to the dict
        title = str(match.group())
        dont_Matches_Dict[coordinate] = title


    # pprint.pprint(dont_Matches_Dict)
    return(dont_Matches_Dict)




def get_Pairs(content,Matches_Dict):


    pattern = re.compile('mul\(\d+,\d+\)') # search pattern
    matches = pattern.finditer(content) 

    for match in matches: 

        # print(match.start(), match.group())

        coordinate = int(match.end()) # get each matches coordinat and name (i.e., mel(X,Y)) and append them to the dict
        title = str(match.group())

        Matches_Dict[coordinate] = title


    return Matches_Dict



def remove_dont_pairs(sorted_dict):
    final_List= []
    do_or_Dont = ""

    for item in sorted_dict.values():

        if item == "do()" or item == "don't()":
            print(item)
            do_or_Dont = item
            continue

        else:
            if item != "do()" and item != "don't()":

                if do_or_Dont != "don't()":
                    final_List.append(item)
                    print(item)

                else:
                    print(f"REMOVING {item}")
                    continue
    # print(final_List)
    return final_List

        


content = openFile("../input/data3") #open file and parse data3.txt

matchesDict = get_do(content) # get do()'s
matchesDict = get_dont(content,matchesDict) #get don't()'s
matchesDict = get_Pairs(content,matchesDict) #get mul(X,Y)'s



sorteddict = sorted(matchesDict.items(), key= lambda x:x[0])
convertdict = dict(sorteddict)
# pprint.pprint(convertdict)

# pprint.pprint(sorteddict)
final_List = remove_dont_pairs(convertdict)

final_Sum = getmul(str(final_List))

print(f"Final Number == {final_Sum}")


