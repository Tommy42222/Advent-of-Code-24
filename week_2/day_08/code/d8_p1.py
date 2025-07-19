import os,re,pprint
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

    # pprint.pprint(antennas_locations_dict)
    return antennas_locations_dict






here = os.path.dirname(__name__)
with open (f"{here}../input/sample8.txt", "r") as file:
    content = file.read()
    
def main(content):
    max_grid_bounds_limit = 50


    parsed_content = parse_input(content)
    antennas_coordinates_dict = find_antennas(parsed_content)


    for antenna in antennas_coordinates_dict.values():
        print(antenna)
        pass



main(content)