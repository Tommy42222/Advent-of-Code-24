from collections import defaultdict
import os,pprint



def parce_x_y_input_pairs(content,split_character,is_reversed): # gets each x|y pairs and stores them in a list
    input_content_list = content.splitlines() 

    new_content_list = []

    for item in range(len(input_content_list)):

        if is_reversed == True: # if True, start at the bottom of input and work upwards, else go top to
            item = -item - 1

        if input_content_list[item] == "": # stops iteration at the end of the x|y column
            break

        else:
            temp = str(input_content_list[item]) # stores the Nth row in temp
            row = temp.split(split_character) 
            new_content_list.append(row)

    return list(new_content_list)




def create_X_Y_deafultdict(input_list): 

    x_y_Dict:dict = defaultdict(lambda:[[],[]]) # create a defultdict with a [[],[]] empty 2d list as the value format


    for item in range(len(input_list)): # appends all tokens that come after X

        x,y = pair_list[item][0], pair_list[item][1]
        x_y_Dict[x][0].append(y)


    for item in range(len(input_list)): # appends all tokents that X must come before

        x,y = pair_list[item][0], pair_list[item][1]

        if y in x_y_Dict.keys():
            x_y_Dict[y][1].append(x)
    

    return x_y_Dict





here = os.path.dirname(__file__) # gets the absolute file path of the current file 
with open(f"{here}/../input/sample5.txt","r") as file:
    content = file.read()




pair_list = parce_x_y_input_pairs(content,"|",is_reversed=False) 
instructions_list = parce_x_y_input_pairs(content,",",is_reversed=True) 

'''
 x_y_Dict contains each token as key, and list [[A][B]] as values. 
 [A]: holds all tokens that must come after the key.
 [B]: holds all tokens that the key must come before.
 The total number of tokens in each list [[A][B]] is the same for the sample input
'''
x_y_Dict = create_X_Y_deafultdict(pair_list) 

for row in instructions_list:
    pass




pprint.pprint(x_y_Dict)
pprint.pprint(instructions_list)




