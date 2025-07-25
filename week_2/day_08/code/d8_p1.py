import os,pprint
from collections import defaultdict


def parse_input(file: str): # this takes in the str input, and returns a 2d list containing each row and item
    output = [list(line) for line in file.splitlines()]
    print(output)
    return output
    


def find_antennas(content: list): # this searches a 2d list of all items that is not a "." and stores their Y & X coordinates in a defultdict with the signal as the key, and each coord pair as the values
    antennas_locations_dict:dict = defaultdict(lambda: []) # defult dict format| [ANTENNA_SIGNAL]: [[y,x],[y,x]]... etc

    for column_index,row in enumerate(content):
        for row_index,item in enumerate(row):
            if item != ".":

                coordinates = []
                coordinates.append(column_index)
                coordinates.append(row_index)
                
                antennas_locations_dict[item].append(coordinates)

    pprint.pprint(antennas_locations_dict)
    return antennas_locations_dict



def get_coordinate_differnce(first: list,second: list) -> list[str]: # takes two [Y,X] lists, and returns the differnces between the two X coords and Y coords
    coordinate_differnces = []

    x1 = first[0] 
    y1 = first[1]

    x2 = second[0]
    y2 = second[1]

    x_differnce = (x1 - x2) * -1
    y_differnce = (y1 - y2) * -1

    coordinate_differnces.append(x_differnce)
    coordinate_differnces.append(y_differnce)

    # print(f'INPUT = {first}, {second}')
    # print(f"DIFFERNCE = {coordinate_differnces}")
    return coordinate_differnces



"""
adds the differnce vector onto a given coord and checks:
- if that square is in bounds (no index errors or -1 index looping)
- not already marked as an anti node -> "$"

If both conditions are TRUE, change that grid square to a "$", increment global counter by 1, and return the modifyed grid 
"""
def check_for_anti_node(next_item: list,differnces: list,grid: list):
    global total_antinode_couter
    
    new_y_cord = next_item[0] + differnces[0]
    new_x_cord = next_item[1] + differnces[1]

    output_message = ""
    # print(f"NEXT ITEM = {next_item}, DIFF = {differnces}, NEW_CORDS = {new_y_cord}:{new_x_cord}, FREQUANCY = {antenna_frequency}, NEW SPOT = {place_on_grid}")

    if new_x_cord < 0 or new_y_cord < 0: # if -N indexing
        output_message = "less then 0"

    else:
        try:
            place_on_grid = grid[new_y_cord][new_x_cord]

            if place_on_grid == "$": #if space aready has an antinode on it
                output_message = "already taken"

            else:
                output_message = "hit" # if the new square is valid
                total_antinode_couter += 1
                grid[new_y_cord][new_x_cord] = "$"
                

        except IndexError: # if new coords are out of bounds
            output_message = "out of bounds"

    print(f"{output_message:<13} | {new_y_cord}:{new_x_cord}")
    return grid




def iterate_over_antenna_signal(coordinates: list,grid :list) -> None: # iterates over each coord pair, and runs it against all the other pairs in the remaining list
    orginal_coordinates_list = coordinates

    for index,item in enumerate(orginal_coordinates_list):

        temp_list = orginal_coordinates_list[:]
        temp_list.pop(index)
        
        for next_item in temp_list: # for each item in the temp list
            # print(item,next_item)
            
            differences = get_coordinate_differnce(item,next_item)
            check_for_anti_node(next_item,differences,grid)
        print("~~~~~~")


def main(content:str) ->None:

    parsed_content = parse_input(content)
    antennas_coordinates_dict = find_antennas(parsed_content)

    for signal,coordinates in antennas_coordinates_dict.items(): # for each unique [SIGNAL] 

            print(signal.center(22,"-"))
            iterate_over_antenna_signal(coordinates,parsed_content) 
            # print("----------------------")

    



if __name__ == "__main__":
    here = os.path.dirname(__file__)
    with open (f"{here}/../input/input8.txt", "r") as file:
        content = file.read()

    total_antinode_couter = 0
    main(content)
    print(total_antinode_couter)

    


