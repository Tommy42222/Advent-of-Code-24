import sys,os,re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def shift_list_right(input_list):
    input_list.insert(0, input_list.pop())
    return input_list

def get_Match_coords(content,search_Character): # searches a 2d string array, looks for matching characters, and returns their y,x coords as a 2d array.

    match_list = [] # dict to store all matches and their coordinates
    pattern = re.compile(search_Character) 
    matches = pattern.finditer(content) 


    for match in matches: 
        coordinate = int(match.start()) # get each match's coordinates 
        match_list.append(coordinate) 

    return(match_list)



def Search_for_XMAS(x_cord,y_cord,text,target_Characters_list): 
      

 #[---- each Nth column in the lists determines the x and y vectors when searching the text for target characters.
    x_mult_values = [-1,1,1,-1] #|: X_Mults[-1 = backwards, 0 = no direction,  1 = forwards]
    y_mult_values = [-1,-1,1,1] #|: Y_Mults[-1 = downwards, 0 = no direaction, 1 = upwards ]
    direction_values = ["up-left","up-right","bottom-left","bottom-right"] # these help the human understand what each column does
    matches = 0

    for rotations in range(4):
        
        number_of_Hits = 0
        shifted_character_list = shift_list_right(target_Characters_list)
        # print(shifted_character_list)

        for i in range(len(direction_values)): # for each direction the function will check...
            
            
            target_character = shifted_character_list[i]
            # print("--X =",x_cord,"--Y =",y_cord,"--X_mult =",x_mult_values[i],"--Y_mult =",y_mult_values[i],"--Direction =",[direction_values[i]],target_character)

            number_of_Hits += check_direction(x_cord,y_cord,x_mult_values[i],y_mult_values[i],text,target_character) # uses the gatherd data to search a given angle from the X for matches
            

        if number_of_Hits == 4:
            matches += 1
            print("Match")

        else:
            print(f"Fail: number of hists >>> {number_of_Hits}")
            continue
    return matches



def check_direction(x_cord,y_cord,x_mult,y_mult,text,target_Character): #function checks characters around the target X for matchs to the list

    try:
        for i in range(1,len(target_Character)+1): # for each letter, the program checks further away from X in the chosen direction

            next_X_coordinate = x_cord + (i * x_mult) 
            next_Y_coordinate = y_cord + (i * y_mult)


            if next_Y_coordinate < 0: # makes sure there is no text wrapping that could mess up the counting
                print("y is less then 0")
                return 0
            
            if next_X_coordinate < 0:
                print("X is less then 0")
                return 0

        
            bool_value = text[y_cord + (i * y_mult)][x_cord + (i * x_mult)] == target_Character[i-1] #checks if the new character match's the Nth character in target_Characters

            # more visual guides for humans
            print("X",x_cord + (i * x_mult),"Y",y_cord + (i * y_mult),"| i =",i,"Target =", target_Character, "Hit >",text[y_cord + (i * y_mult)][x_cord + (i * x_mult)])
            # print(bool_value, target_Character[i-1])
            
            if bool_value == False: # if there is any non-matchs, then this direction won't match 
                return 0

        # print("Match")
        return 1


    except IndexError: # catches any time the function index's an outoff range [index]
        # print("error")
        return 0


here = os.path.dirname(__file__)




newfile = file.splitlines()

# newfile = [i[:10] for i in file.splitlines()[:10]]




number0fRows = file.count("\n") 
number0fRows = len(newfile)
# print(f"NUMBER OF ROWS = {number0fRows}")



match_coord_List = []

for row in range (number0fRows): # for each row in the data, gather the cordinates of the targets character and append them to match_coord_List
     match_coord_List.append(get_Match_coords(newfile[row],search_Character="A"))


number_of_Hits = 0


for row in range(0,number0fRows):  # for each row of data...
    # print(f"Row__{row}__{match_coord_List[row]}")    # prints an overview of that row of coordinates
    for item in range(0,len(match_coord_List[row])):  # for each coordinate in that row...
        
        x_Location = match_coord_List[row][item]

            # gather that coordinate...
        number_of_Hits += Search_for_XMAS(x_Location,row,newfile,target_Characters_list=["M","M","S","S",]) # calls the main search function, target character list is checking clockwise starting in the top left

        # print(f"Current Total = {number_of_Hits}")

print(f"Final Total = {number_of_Hits}")



