import sys,os,re,time,pprint
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.homeGrownFunctions import openFile

def get_Match_coords(content,search_Character):

    x_Match_list = [] # dict to store all matches and their coordinates
    pattern = re.compile(search_Character) # search pattern
    matches = pattern.finditer(content) 

    for match in matches: 

        coordinate = int(match.start()) # get each matches coordinat and name (i.e., do()) and append them to the dict
        x_Match_list.append(coordinate)

    return(x_Match_list)



def Search_for_XMAS(x_cord,y_cord,text,target_Characters_list):

    x_mult_values = [-1,0,1,-1,0,1,1,-1]
    y_mult_values = [-1,-1,-1,1,1,1,0,0]
    direction_values = ["up-left","up","up-right","bottom-left","bottom","bottom-right","left","right"]
    number_of_Hits = 0

    for i in range(len(direction_values)):
       
        # print(" ")
        # print("X =",x_cord,"Y =",y_cord,"---",x_mult_values[i],y_mult_values[i],[direction_values[i]])
        
        number_of_Hits += check_angle(x_cord,y_cord,x_mult_values[i],y_mult_values[i],text,target_Characters_list)

    return number_of_Hits



def check_angle(x_cord,y_cord,x_mult,y_mult,text,target_Characters_list):
    target_Characters = target_Characters_list

    try:
        for i in range(1,len(target_Characters_list)+1):
            x = x_cord + (i * x_mult)
            y = y_cord + (i * y_mult)
            # print(x,y)
            if y < 0:
                # print("y is less then 0")
                return 0
            
            if x < 0:
                # print("X is less then 0")
                return 0

            

            # print("X",x_cord + (i * x_mult),"Y",y_cord + (i * y_mult),"| i =",i)
            bool_value = text[y_cord + (i * y_mult)][x_cord + (i * x_mult)] == target_Characters[i-1]
            # print(bool_value, target_Character[i-1])
            
            if bool_value == False:
                return 0

        # print(bool_list)
        print("Match")
        return 1



    except IndexError:
        # print("error")
        print(f"error")
        return 0






file = openFile("data4")

newfile = file.splitlines()

horizontal_Matches = 0
number0fRows = file.count("\n") 
print(f"NUMBER OF ROWS = {number0fRows}")



match_coord_List = []
for row in range (number0fRows):
     match_coord_List.append(get_Match_coords(newfile[row],search_Character="X"))

number_of_Hits = 0

for row in range(0,number0fRows):
    print(f"Row__[{row}]_{match_coord_List[row]}")
    for item in range(0,len(match_coord_List[row])):
    
        x_Location = match_coord_List[row][item]

        x_Character = (newfile[row][x_Location])


        number_of_Hits += Search_for_XMAS(x_Location,row,newfile,target_Characters_list=["M","A","S",])
        

        

   
    print(f"Current Total = {number_of_Hits}")

print(f"Final Total = {number_of_Hits}")

   




