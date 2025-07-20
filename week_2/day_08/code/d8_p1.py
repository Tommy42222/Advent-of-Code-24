import os,pprint
from collections import defaultdict

def parse_input(file):
    output = file.splitlines()
    return output
    

def find_antennas(content):
    antennas_locations_dict:dict = defaultdict(lambda: [])

    for column_index,row in enumerate(content):
        for row_index,item in enumerate(row):
            if item != ".":

                coordinates = []
                coordinates.append(column_index)
                coordinates.append(row_index)
                
                antennas_locations_dict[item].append(coordinates)

    pprint.pprint(antennas_locations_dict)
    return antennas_locations_dict



def get_coordinate_differnce(first,second):
    coordinate_differnces = []

    print(f'INPUT = {first}, {second}')
    x1 = first[0] 
    y1 = first[1]

    x2 = second[0]
    y2 = second[1]

    x_differnce = (x1 - x2) * -1
    y_differnce = (y1 - y2) * -1

    coordinate_differnces.append(x_differnce)
    coordinate_differnces.append(y_differnce)

    print(f"DIFFERNCE = {coordinate_differnces}\n")
    return coordinate_differnces



def iterate_over_antenna_signal(coordinates):
    orginal_coordinates_list = coordinates

    for index,item in enumerate(orginal_coordinates_list):

        temp_list = orginal_coordinates_list[:]
        temp_list.pop(index)
        
        for next_item in temp_list:
            # print(item,next_item)
            
            differences = get_coordinate_differnce(item,next_item)


def check_for_anti_node(next_item,differnces,grid):
    pass



def main(content):

    max_grid_bounds_limit = 50

    parsed_content = parse_input(content)
    antennas_coordinates_dict = find_antennas(parsed_content)


    for signal,coordinates in antennas_coordinates_dict.items():

            print(signal)
            iterate_over_antenna_signal(coordinates)
            print("-------")



here = os.path.dirname(__name__)
with open (f"{here}../input/input8.txt", "r") as file:
    content = file.read()
    
main(content)

