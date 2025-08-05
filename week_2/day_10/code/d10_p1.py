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
                
    # print(starting_locations)
    return starting_locations
                


def check_neighbours(current_location: tuple, to_vist_stack: set, visted:list, grid:list) -> set:
    print("---")
    y_cord = current_location[0]
    x_cord = current_location[1]
    # print(f"input = {(y_cord,x_cord)}")


    current_hight = int(grid[y_cord][x_cord])

    # these start at north and go clockwise
    y_change = [1,0,-1,0]
    x_change = [0,1,0,-1]

    for direction in range(len(y_change)):
        new_x_cord = x_cord + x_change[direction]
        new_y_cord = y_cord + y_change[direction]

        if new_x_cord < 0 or new_y_cord < 0:
            # print(loc,"loop around")
            continue

        try:
            loc = (new_y_cord,new_x_cord)
            if loc in visted:
                # print(loc,"visited")
                continue

            if int(grid[new_y_cord][new_x_cord]) == current_hight + 1:
            
                # print((new_y_cord,new_x_cord),"added")  
                to_vist_stack.add((loc))
        
        except:
            # print(loc,'error')
            continue
    
    # print("tv",to_vist_stack)
    # print("v",visted)
    return to_vist_stack



def dfs(location: tuple ,to_vist: set[tuple], visted: list, grid:list):
    counter = 0

    visted.append(location)
    to_vist = check_neighbours(location,to_vist,visted,grid)

    while to_vist:

        location = to_vist.pop()
        
        if grid[location[0]][location[1]] == "9":
            print("FOUND A 9!")
            counter += 1

        visted.append(location)
        to_vist = check_neighbours(location,to_vist,visted,grid)


    print(f"final count {counter}")
    return counter


def main() -> None:
    grid = parse_input(content)
    pprint(grid)
    starting_locations = find_all_starting_locs(grid)

    count = 0

    for location in starting_locations:
        to_vist = set()
        visted = []
        count += dfs(location,to_vist,visted,grid)

    print(count)



if "__main__" == __name__:

    here = os.path.dirname(__file__)
    with open (f"{here}/../input/sample10.txt", "r") as file:
        content = file.read()

    main()