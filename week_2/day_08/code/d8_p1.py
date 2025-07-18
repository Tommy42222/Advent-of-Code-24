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

                coordinates = f"{column_index}:{row_index}"
                antennas_locations_dict[item].append(coordinates)

    pprint.pprint(antennas_locations_dict)
    return antennas_locations_dict




here = os.path.dirname(__name__)
with open (f"{here}../input/input8.txt", "r") as file:
    content = file.read()

parsed_content = parse_input(content)
find_antennas(parsed_content)