import os,pprint
from collections import defaultdict


def parse_input(file):
    output = [list(line) for line in file.splitlines()]
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



def check_for_anti_node(next_item,differnces,grid,antenna_frequency):
    global total_antinode_couter
    
    map_grid = grid

    new_y_cord = next_item[0] + differnces[0]
    new_x_cord = next_item[1] + differnces[1]

    output_message = "out of bounds"
    # print(f"NEXT ITEM = {next_item}, DIFF = {differnces}, NEW_CORDS = {new_y_cord}:{new_x_cord}, FREQUANCY = {antenna_frequency}, NEW SPOT = {place_on_grid}")

    if new_x_cord < 0 or new_y_cord < 0:
        output_message = "less then 0"

    else:
        try:
            place_on_grid = map_grid[new_y_cord][new_x_cord]

            if place_on_grid == "$":
                output_message == "space already taken"

            else:
                output_message == "hit"
                total_antinode_couter += 1
                map_grid[new_y_cord][new_x_cord] = "$"
                

        except IndexError:
            pass

    print(f"{output_message:<13} | {new_y_cord}:{new_x_cord}")
    return map_grid



def iterate_over_antenna_signal(coordinates,grid,singal):
    orginal_coordinates_list = coordinates

    for index,item in enumerate(orginal_coordinates_list):

        temp_list = orginal_coordinates_list[:]
        temp_list.pop(index)
        
        for next_item in temp_list:
            # print(item,next_item)
            
            differences = get_coordinate_differnce(item,next_item)
            grid = check_for_anti_node(next_item,differences,grid,singal)


    return grid




def main(content):
    parsed_content = parse_input(content)
    antennas_coordinates_dict = find_antennas(parsed_content)

    for signal,coordinates in antennas_coordinates_dict.items():

            print(signal)
            grid = iterate_over_antenna_signal(coordinates,parsed_content,signal)
            print("----------------------")

    



if __name__ == "__main__":
    here = os.path.dirname(__file__)
    with open (f"{here}/../input/input8.txt", "r") as file:
        content = file.read()

    total_antinode_couter = 0
    main(content)
    print(total_antinode_couter)

    


