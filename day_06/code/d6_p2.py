import os,re,pprint
from collections import Counter


def parse_input(input_file): # returns the grid as a  2d list with each characters as an item in the list
    return [list(line) for line in input_file.splitlines()]


def place_guard_back_on_grid(grid): # places the guards back on the grid after part 1
    start_x_cord = starting_info[1]
    start_y_cord = starting_info[2]
    grid[start_y_cord][start_x_cord] = "^"
    return grid

def write_grid_to_txt(grid): # used to create grid for part 2
    part_2_grid = "\n".join("".join(map(str, row)) for row in grid)
    with open(f"../input/sample6_p2.txt","w") as file:
        file.write(part_2_grid)


def get_guard_starting_location(grid): #searches the grid for for guards token, returns the guards x,y coordinates
    guard_start_token = "^"

    for row_index,row in enumerate(grid):
        for guard in guard_start_token: # searches each row for the guard

            if guard in row: 
                
                column_index = row.index(guard) 
                
                return guard, column_index,row_index

            continue



def turn_90_deg_right(turn_count,direction_list): 
    turn_count += 1
    new_facing_direction = direction_list[turn_count % 4]
    

    return new_facing_direction, turn_count



def move_one_step_forward(x_cord,y_cord,x_cord_change,y_cord_change): # moves the guards forward one square based on their current facing direction
    new_x_cord = x_cord + x_cord_change[0]
    new_y_cord = y_cord + y_cord_change[0]

    return new_x_cord,new_y_cord



def set_current_square_to_X(grid,x_cord,y_cord):
    grid[y_cord][x_cord] = "@"
    return grid



def check_next_square(grid,x_cord_change,y_cord_change,start_x_cord,start_y_cord): # checks the next square along the guards path for boxs or the egde of the grid
    new_x_cord = start_x_cord + x_cord_change[0]
    new_y_cord = start_y_cord + y_cord_change[0]

    if new_x_cord < 0 or new_y_cord < 0:
        print("WOULD LOOP AROUND...")
        return -1
    try:
        
        next_grid_square = grid[new_y_cord][new_x_cord]
        # print(next_grid_square)

        if next_grid_square != "#":
            return True
        else:
            return False
        
    except: 
        IndexError
        print("OUT OF INDEX RANGE")
        return -1



def main(input_grid,starting_info,movement_directions,movement_directions_list):
  
    
    # starting grid
    main_grid = input_grid

    # the starting coords for the guard, these will get updated each time the guard moves
    x_coord = starting_info[1]
    y_coord = starting_info[2]

    # counts the number of times the guard turns to the right
    turn_count = 0

    # maps guard token to direction (up,down,left,right)
    current_facing_direction = movement_directions_list[turn_count % 4]
    
           
    turn_tracker_list = []  # adds and stores the coordinates of the guard each time their turn, if duplecate coords are detected, then a loop is found
    turn_tracker_buffer = [] # max len of 2, when len = 2: check if they are the same| if yes add that coord only once to ttl and empty buffer| otherwise pop item[0] to ttl and repeat
        

    while True: # loops until the guard looks off the grid, then it returns the final grid 

        # values added to the x and y cords to move the guard in their current facing direction 
        x_coord_direction_change = movement_directions[current_facing_direction][1]
        y_coord_direction_change = movement_directions[current_facing_direction][0]


        # checks if the next square is empty, a box, or the egde of the grid (returns Ture or False or 0)
        bool_output = check_next_square(main_grid,x_coord_direction_change,y_coord_direction_change,x_coord,y_coord)
        
        # replaces the guards current square with a ?
        set_current_square_to_X(main_grid,x_coord,y_coord)



        if bool_output == -1: # if out of grid bounds: return grid and terminate "main"
            # print("out of bounds")
            return main_grid
        

        elif bool_output == False: # if box: turn 90deg right, and run the code for part 2

            current_facing_direction,turn_count = turn_90_deg_right(turn_count,movement_directions_list)
            
            turn_coordinates = f"{y_coord}:{x_coord}"
            
            # print(f"Turning to face {current_facing_direction}, count = {turn_count}, coords = {turn_coordinates}")

            turn_tracker_buffer,buffer_output = prosses_buffer(turn_tracker_buffer,turn_coordinates)
            
            if buffer_output == None: # don't check for loop if buffer returns no value
                continue

            turn_tracker_list.append(buffer_output)
            bool_check_loop = check_for_loop(turn_tracker_list)
            
            if bool_check_loop == True:
                print("LOOP FOUND")
                return True
            

            

        elif bool_output == True: # if empty: move one step fowrard
            # print(f"Moving >>> {current_facing_direction}")

            x_coord,y_coord = move_one_step_forward(x_coord,y_coord,x_coord_direction_change,y_coord_direction_change)
            continue

#----------------------------------------------------------------------------------------

def prosses_buffer(buffer,input_coord): 

    if len(buffer) == 2: # if the buffer is full
        first = buffer[0]
        second = buffer[1]

        if first == second: # if matching pair, return the [0] value and clear buffer
            output_value = first
            buffer.clear()
            buffer.append(input_coord)

        else:
            output_value = first # if no match, pop and return the [0] value
            buffer.pop(0)
            buffer.append(input_coord)

    else:
        buffer.append(input_coord) # if the buffer is not full, return None
        output_value = None

    return buffer,output_value 



def check_for_loop(input_list): # this list stores all the cooridinates of each turn the guard makes, if any duplicates are found, then the guard is stuck in a loop. 
    item_counter = Counter(input_list).items()
    
    for coordinate in item_counter:
        if coordinate[1] >= 2:
            
            print(item_counter)
            print(coordinate)
            return True
    
    return False
    




def get_Match_coords(content,search_Character): # searches a 2d string array, looks for matching characters, and returns their y,x coords as a 2d array.

    match_list = [] # dict to store all matches and their coordinates
    pattern = re.compile(f"\?") 
    matches = pattern.finditer(content) 


    for match in matches: 
        coordinate = int(match.start()) # get each match's coordinates 
        match_list.append(coordinate) 

    # print(match_list)
    return(match_list)


def place_box_in_guard_path(grid,location):
    original_grid = grid

    temp_grid = original_grid[:]
    temp_grid = temp_grid[:location] + "#" + temp_grid[location + 1:]

    # print(temp_grid)
    return temp_grid



""" ORDER OF OPERATIONS FOR GUARD MOVMENT ALGORITHOM
1: get the guards current x and y cords
2: get current facing direction or CFD

3: change the grid square the guard is on to an "X"
4: check the next grid square in its path based on its CFD

5: turn 90 deg right if the square is a #, update the CFD, repeat steps until the path ahead is not blocked
6: move/update the guards current x and y cords based on CFD and Repeat all stepts above
"""
        

if __name__ == "__main__":

    here = os.path.dirname(__file__)
    with open(f"{here}/../input/input6_p2.txt","r") as file:
        content = file.read()
    
    facing_directions_list = ["up","right","down","left"]
    movement_directions_dict = {"up":[[-1],[0]],"down":[[1],[0]],"left":[[0],[-1]],"right":[[0],[1]]} # dict format = "Direction": [Y_change][X_change]
    
    loop_counter = 0

    guard_path_coords = get_Match_coords(content,"?")

    i = 0
    for location in guard_path_coords:
        i += 1
        itterated_content = place_box_in_guard_path(content,location)



        grid = parse_input(itterated_content)
        starting_info = get_guard_starting_location(grid)

 


        final_output_count = main(grid,starting_info,movement_directions_dict,facing_directions_list)

        print(f"---------------------------------* location No.{i}")
        if final_output_count == True:
            loop_counter += 1
            continue

        # pprint.pprint(final_output_count)
        # print(sum(X.count("@") for X in final_output_count))

print(F"FINAL NUMBER OF LOOPS FOUND = {loop_counter}")



