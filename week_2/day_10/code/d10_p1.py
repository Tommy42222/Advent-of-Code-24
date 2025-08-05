import os
from pprint import pprint


def parse_input(text_input) -> list:
    return [list(line) for line in text_input.splitlines()]


def find_all_starting_locs(grid): # this returns a list of tuples (y_cord,x_cord)
    starting_locations = []
    for row_index, row in enumerate(grid):
        for item_index, item in enumerate(row):
            if item == "0":
                starting_locations.append((row_index,item_index))
                
    print(starting_locations)
    return starting_locations
                


def check_neighbours(current_location: tuple, stack: list, grid:list) -> set:
    y_cord = current_location[0]
    x_cord = current_location[1]

    current_hight = int(grid[y_cord][x_cord])

    y_change = [1,0,-1,0]
    x_change = [0,1,0,-1]

    for direction in range(len(y_change)):
        new_x_cord = x_cord + x_change[direction]
        new_y_cord = y_cord + y_change[direction]

        if new_x_cord < 0 or new_y_cord < 0:
            print("loop around")
            continue

        try:
            if int(grid[new_y_cord][new_x_cord]) == current_hight + 1:
                # print(grid[new_y_cord][new_x_cord])  
                stack.append((new_y_cord,new_x_cord))
        

        except IndexError:
            print('out of bounds')
            continue
    
    print(stack)
    return stack



def main() -> None:
    grid = parse_input(content)
    starting_locations = find_all_starting_locs(grid)
    visted = []

    for sl in starting_locations:
        check_neighbours(sl,visted,grid)



if "__main__" == __name__:

    here = os.path.dirname(__file__)
    with open (f"{here}/../input/sample10.txt", "r") as file:
        content = file.read()

    main()