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
        x_y_Dict[x][1].append(y)


    for item in range(len(input_list)): # appends all tokents that X must come before

        x,y = pair_list[item][0], pair_list[item][1]

        x_y_Dict[y][0].append(x)
    

    return x_y_Dict





def check_row(row,x_y_pair):
    bool_after = None
    bool_before = True

    for item in range(len(row)):
        if item == 0:
            # only check after x
            bool_after = check_after_X(item,x_y_pair,row)
            

        else:
            bool_before = check_before_X(item,x_y_pair,row)
            bool_after = check_after_X(item,x_y_pair,row)
            
        print(f"{bool_before = } {bool_after = }")
        if bool_before == False or bool_after == False:
            
            print("FAIL ROW")
            return False

    print("SAFE ROW")
    return True


def check_after_X(token_location,x_y_pair,row):
    # for all items before the token
    token = row[token_location]
    row_length = len(row)

    for i in range(token_location + 1,row_length):
        find_value = row[i]


        bool_value = find_value in x_y_pair[token][1]
        if bool_value == False:

            return False
        else:
            continue

    return True



def check_before_X(token_location,x_y_pair,row):
    # for all items before the token
    token = row[token_location]


    for i in range(0,token_location):
        find_value = row[i]

        bool_value = find_value in x_y_pair[token][0]
        if bool_value == False:

            return False
        else:
            continue
        

    return True


def return_row_value(success,row):
    row_size = len(row)
    if success == True:
        return int(row[(row_size//2)])
    
    else:
        return 0
    



here = os.path.dirname(__file__) # gets the absolute file path of the current file 
with open(f"{here}/../input/sample5.txt","r") as file:
    content = file.read()




pair_list = parce_x_y_input_pairs(content,"|",is_reversed=False) 
instructions_list = parce_x_y_input_pairs(content,",",is_reversed=True) 

'''
 x_y_Dict with each token as key, and list [[A][B]] as values. 
 [A]: holds all tokens that must come BEFORE the key.
 [B]: holds all tokens that must come AFTER the key.
 The total number of tokens in each list [[A][B]] is the same for the sample input
'''
x_y_Dict = create_X_Y_deafultdict(pair_list) 
final_count = 0
for row in instructions_list:

    print("\n")
    print(f"ROW ={row}")
    bool_value = check_row(row,x_y_Dict)
    final_count += return_row_value(bool_value,row)

print(f"\nFinal count = {final_count}")
pprint.pprint(x_y_Dict)
