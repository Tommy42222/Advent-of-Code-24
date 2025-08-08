import os
from pprint import pprint


def parse_input(text_input: str) -> list:
    return [list(line) for line in text_input.splitlines()]


def find_all_starting_locs(grid: list[str]):  # this returns a list of coordinates as tuples (y_cord,x_cord)
    starting_locations = []
    for row_index, row in enumerate(grid):
        for item_index, item in enumerate(row):
            if item == "0":
                starting_locations.append((row_index, item_index))

    # print(starting_locations)
    return starting_locations


"""
This function checks the horizontally & vertically adjacent squares around the current_location
for valid paths, then appends then to the top of the "to_visit" stack.

A path is valid only if"
    - its height value is 1 greater the current_location
    - it is a path that has not already been visited before

Any path that fails to meet these 2 rules are not appended
"""
def check_neighbours( 
    current_location: tuple[int, int],
    to_vist_stack: list[tuple[int, int]],
    visted: list[tuple[int, int]],
    grid: list[str]) -> set:

    # print("---")
    y_cord = current_location[0]
    x_cord = current_location[1]

    current_height = int(grid[y_cord][x_cord])

    # these directions start at north and go clockwise
    y_change = [1, 0, -1, 0]
    x_change = [0, 1, 0, -1]

    for direction in range(len(y_change)):  # checks each adjacent sqaure
        new_x_cord = x_cord + x_change[direction]
        new_y_cord = y_cord + y_change[direction]

        new_location = (new_y_cord, new_x_cord)

        if new_x_cord < 0 or new_y_cord < 0:  # prevents index wrap arounds
            continue

        # if new_location in visted:  # don't add already visited locations
        #     continue

        try:
            if int(grid[new_y_cord][new_x_cord]) == current_height + 1:  # only add squares that have a height index of N+1
                to_vist_stack.append((new_location))

        except:  # catchs INDEX and TYPE errors
            continue

    # print("to vist =",to_vist_stack)
    # print("visted =",visted)
    # print("---")
    return to_vist_stack


"""
    - This fucniton perfoms an iterative Depth_First_Search on the grid from the "0" starting point 
"""


def run_DFS(
    location: tuple[int, int],
    to_vist: list[tuple[int, int]],
    visted: list[tuple[int, int]],
    grid: list[str]) -> int:
    
    counter = 0

    visted.append(location)
    to_vist = check_neighbours(location, to_vist, visted, grid)

    while to_vist:  # break when there are no nodes left to visit

        location = to_vist.pop()
        visted.append(location)
        to_vist = check_neighbours(location, to_vist, visted, grid)

        if grid[location[0]][location[1]] == "9":
            # print("found 9")
            counter += 1

    return counter


def main() -> None:
    grid = parse_input(content)
    starting_locations = find_all_starting_locs(grid)

    trailhead_counter = 0
    for location in starting_locations:

        # reset trackers for each starting point
        to_vist = []
        visted = []

        trailhead_counter += run_DFS(location, to_vist, visted, grid)
    print(f"FINAL TRAILHEAD COUNT = {trailhead_counter}")


if "__main__" == __name__:

    here = os.path.dirname(__file__)
    with open(f"{here}/../input/input10.txt", "r") as file:
        content = file.read()

    main()
