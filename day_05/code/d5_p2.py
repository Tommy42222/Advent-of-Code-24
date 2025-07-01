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





def check_row(row,x_y_pair,if_reorder):
    bool_after = None
    bool_before = True

    if len(row) == 0:
        return 0

    for item in range(len(row)): # for each item in the row
        if item == 0:
            # for the first item only check after item
            bool_after = check_after_X(item,x_y_pair,row)
            

        else:
            bool_before = check_before_X(item,x_y_pair,row)
            bool_after = check_after_X(item,x_y_pair,row)
            
        # print(f"{bool_before = } {bool_after = }")
        if bool_before == False or bool_after == False:
            
            print("FAIL ROW")
            return False

    print("SAFE ROW")
    return True


def check_after_X(token_location,x_y_pair,row):

    token = row[token_location]
    row_length = len(row)

    for i in range(token_location + 1,row_length): # for all items after the token
        find_value = row[i]


        bool_value = find_value in x_y_pair[token][1]
        if bool_value == False:
            return 0
        else:
            continue
    return True



def check_before_X(token_location,x_y_pair,row):

    token = row[token_location]


    for i in range(0,token_location): # for all items before the token
        find_value = row[i]

        bool_value = find_value in x_y_pair[token][0]
        if bool_value == False:
            return 0
        else:
            continue
        
    return True


def return_row_value(success,row):
    if success == False:
        return row
    else:
        return "0"
    

def swap_list_pair(token,find_value,row):

    row[token], row[find_value] = row[find_value], row[token]

    print(f"SWAPPED", end=" --- ")
    print(row[token],">",row[find_value])
    

    return row


def recheck_pair(iteration,token,x_y_pair,item,compere_token):
              
            if item == iteration: # dont check the same index as the token
                # print("++++")
                return None
                
            elif item < iteration: # items before
                # print(f"{token,compere_token} <<< {iteration}", end=" ")
                bool_value = compere_token in x_y_pair[token][0]


            elif item > iteration: # items after
                # print(f"{token,compere_token} >>> {iteration}", end=" ")
                bool_value = compere_token in x_y_pair[token][1]
            
            # print(bool_value)
            return bool_value


def reorder_row(row,x_y_pair):

    print("INPUT =",row)    
    row_length = len(row)

    for iteration in range(row_length): # loop for each index in row


        
        # print(f" iteration = {iteration} Token = {token}")
        
        while True: # loop until index_N is safe, then loop through index_N+1
            token = row[iteration]
            counter = 0
            for item in range(row_length): # loop over each item in list, getting smaller with each "iteration"
                
                compere_token = row[item]
                token_index = row.index(token)

                # print(token,compere_token)

                bool_output = recheck_pair(iteration,token,x_y_pair,item,compere_token)


                if bool_output == False:
                    # print(f"\nBEFORE {row}")
                    row = swap_list_pair(token_index,item,row)
                    # print(f"AFTER {row}")
                    continue

                elif bool_output == True or bool_output == None:
                    counter += 1

            if counter == row_length:
                break  
            else:
                continue
            

    print(f"OUTPUT {row}")
    return row  


            

def get_sotred_row(row,x_y_pair):

    bool_after = None
    bool_before = True

    if len(row) == 0:
        return 0

    new_sorted_row = reorder_row(row,x_y_pair)
    return new_sorted_row





here = os.path.dirname(__file__) # gets the absolute file path of the current file 
with open(f"{here}/../input/input5.txt","r") as file:
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
incorect_list = []
for row in instructions_list:

    print("\n")
    print(f"ROW ={row}")

    bool_value = check_row(row,x_y_Dict,if_reorder=False)

    incorect_row = return_row_value(bool_value,row)
    incorect_list.append(incorect_row)

# print(f"\nFinal count = {final_count}")
pprint.pprint(x_y_Dict)
pprint.pprint(incorect_list)
print("end of part one\n---\n")



for new_row in incorect_list:
    
    output = get_sotred_row(new_row,x_y_Dict)

    value  = int(output[len(output)//2])
    print(f"MIDDLE VALUE = {value}\n-------------------------")
    final_count += value
print(f"FINAL COUNT = {final_count}")
