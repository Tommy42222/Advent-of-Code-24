import os,pprint



def parse_input(input_file):
    return [list(line) for line in input_file.splitlines()]


def get_guard_starting_location(grid):
    guard_start_token = "^"

    for row_index,row in enumerate(grid):
        for guard in guard_start_token: # searches each row for matches in token_keys

            if guard in row: 
                
                column_index = row.index(guard) 
                
                return guard, column_index,row_index

            continue




def main(input_grid,starting_info,movement_directions,movement_directions_list):
  
    # NOTE Y_CORD COMES BEFORE X_CORD WHEN INDEXING THE GRID: REMEMBER XMAS...
    
    # starting grid
    main_grid = input_grid

    # guard token (^,>,<,v) and its starting x and y cords
    guard_token = starting_info[0]
    x_cord = starting_info[1]
    y_cord = starting_info[2]

    turn_count = 0



    # maps guard token to direction (up,down,left,right)
    current_facing_direction = movement_directions_list[turn_count % 4]

    print(current_facing_direction)
    print(f"y = {y_cord},x = {x_cord}")



    while True:


         # values added to the x and y cords to move the guard in their current facing direction 
        x_cord_direction_change = movement_directions[current_facing_direction][1]
        y_cord_direction_change = movement_directions[current_facing_direction][0]

        print(f"Y = {y_cord_direction_change},X = {x_cord_direction_change}")
        print(f"Looking >>> {current_facing_direction}")

        
        # checks if the next square is empty, a box, or the egde of the grid (returns Ture or False or 0)
        bool_output = check_next_square(main_grid,x_cord_direction_change,y_cord_direction_change,x_cord,y_cord)
        set_current_square_to_X(main_grid,x_cord,y_cord)

        if bool_output == -1: # if out of grid bounds
            print("out of bounds")
            pprint.pprint(main_grid)
            
            return main_grid

        elif bool_output == False: # if box
            print("HIT A BOX!")
            current_facing_direction,turn_count = turn_90_deg_right(turn_count,movement_directions_list)
            pprint.pprint(main_grid)

            continue

        elif bool_output == True: # if empty

 

            x_cord,y_cord = move_one_step_forward(x_cord,y_cord,x_cord_direction_change,y_cord_direction_change)
            continue

        


def turn_90_deg_right(turn_count,direction_list):
    turn_count += 1
    new_facing_direction = direction_list[turn_count % 4]
    
    print(f"Turning to face {new_facing_direction}, count = {turn_count}\n")
    return new_facing_direction, turn_count




def move_one_step_forward(x_cord,y_cord,x_cord_change,y_cord_change):

    new_x_cord = x_cord + x_cord_change[0]
    new_y_cord = y_cord + y_cord_change[0]

    print(f"moving from (X = {x_cord} Y = {y_cord}) to X = {new_x_cord} Y = {new_y_cord}\n")

    return new_x_cord,new_y_cord



def set_current_square_to_X(gird,x_cord,y_cord):
    gird[y_cord][x_cord] = "X"
    return grid


def check_next_square(grid,x_cord_change,y_cord_change,start_x_cord,start_y_cord):

    print(start_y_cord,start_x_cord)
    

    new_x_cord = start_x_cord + x_cord_change[0]
    new_y_cord = start_y_cord + y_cord_change[0]

    print(new_y_cord,new_x_cord)


    if new_x_cord < 0 or new_y_cord < 0:
        print("LESS THEN 0")
        return -1
    try:
        
        next_grid_square = grid[new_y_cord][new_x_cord]
        print(next_grid_square)

        if next_grid_square != "#":
            return True
        else:
            return False
        
    except:
        return -1





""" order of operations for guard
1: get the guards current x and y cords
2: get current facing direction or CFD

3: check the next grid square in its path based on its CFD
4: turn 90 deg right if the square is a #, update the CFD, repeat steps until the path ahead is not blocked

5: change the grid square the guard is on to an "X"
6: move/update the guards current x and y cords based on CFD and Repeat all stepts above
"""


here = os.path.dirname(__file__)
with open(f"{here}/../input/sample6.txt","r") as file:
    content = file.read()

facing_directions_list = ["up","right","down","left"]
movement_directions_dict = {"up":[[-1],[0]],"down":[[1],[0]],"left":[[0],[-1]],"right":[[0],[1]]} # dict format = "Direction": [Y_change][X_change]


grid = parse_input(content)
starting_location = get_guard_starting_location(grid)


output = main(grid,starting_location,movement_directions_dict,facing_directions_list)

print(sum(X.count("X") for X in output))