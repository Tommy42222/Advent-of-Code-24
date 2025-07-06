import os,pprint



def parse_input(input_file):
    grid = input_file
    output_grid_dict = grid.splitlines()

    return output_grid_dict


def get_guard_starting_location(grid,guard_tokens):
    token_keys = [key for key in guard_tokens.keys()]

    for row_index,row in enumerate(grid):
        for guard in token_keys: # searches each row for matches in token_keys

            if guard in row: # assumes guards can't spawn on same row
                
                column_index = row.index(guard) 
                
                return guard, column_index,row_index

            continue




def main(input_grid,starting_info,movement_directions,guard_tokens_list):
  
    # NOTE Y_CORD COMES BEFORE X_CORD WHEN INDEXING THE GRID: REMEMBER XMAS...
    
    # starting grid
    gird = input_grid

    # guard token (^,>,<,v) and its starting x and y cords
    guard_token = starting_info[0]
    start_x_cord = starting_info[2]
    start_y_cord = starting_info[1]

    # maps guard token to direction (up,down,left,right)
    current_facing_direction = guard_tokens_list[guard_token]
    
    # values added to the x and y cords to move the guard in their current facing direction 
    x_cord_direction_change = movement_directions[current_facing_direction][1]
    y_cord_direction_change = movement_directions[current_facing_direction][0]

    print(current_facing_direction)
    print(y_cord_direction_change,x_cord_direction_change)


""" order of operations for guard
1: get the guards current x and y cords
2: get current facing direction or CFD

3: check the next grid square in its path based on its CFD
4: turn 90 deg right if the square is a #, update the CFD, repeat steps until the path ahead is not blocked

5: change the grid square the guard is on to an "X"
6: move/update the guards current x and y cords based on CFD 

>>>Repeat<<<
"""


here = os.path.dirname(__file__)
with open(f"{here}/../input/sample6.txt","r") as file:
    content = file.read()

guard_directions_tokens = {"^":"up",">":"right","v":"down","<":"left"} # if part-two has the guard facing another direction then up
movement_directions = {"up":[[-1],[0]],"down":[[1],[0]],"left":[[0],[-1]],"right":[[0],[1]]} # dict format = "Direction": [Y_change][X_change]


grid = parse_input(content)
starting_location = get_guard_starting_location(grid,guard_directions_tokens)


main(grid,starting_location,movement_directions,guard_directions_tokens)