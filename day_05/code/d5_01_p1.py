from collections import defaultdict
import os,pprint

def parce_x_y_input_pairs(content):

    input_content_list = content.splitlines() 

    new_content_list = []

    for item in range(len(input_content_list)):
        if input_content_list[item] == "": # stops iteration at the end of the x|y column
            break

        else:
            temp = str(input_content_list[item])
            row = temp.split("|")
            new_content_list.append(row)

    return new_content_list

def create_X_Y_deafultdict(input_list): 

    x_y_Dict:dict = defaultdict(lambda:[[],[]]) # create a defultdict with a [[],[]] empty 2d list as the value format

    for item in range(len(input_list)):

        x,y = pair_list[item][0], pair_list[item][1]
        x_y_Dict[x][0].append(y)

    
    for item in range(len(input_list)):

        x,y = pair_list[item][0], pair_list[item][1]

        if y in x_y_Dict.keys():
            x_y_Dict[y][1].append(x)
    
    return x_y_Dict


here = os.path.dirname(__file__) # gets the absolute file path of the current file 
with open(f"{here}/../input/sample5.txt","r") as file:
    content = file.read()


pair_list = parce_x_y_input_pairs(content)
x_y_Dict = create_X_Y_deafultdict(pair_list)


pprint.pprint(x_y_Dict)





