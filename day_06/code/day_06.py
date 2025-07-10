import os



def parse_input(input_file): # returns the grid as a  2d list with each characters as an item in the list
    return [list(line) for line in input_file.splitlines()]



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
    
    print(f"Turning to face {new_facing_direction}, count = {turn_count}\n")
    return new_facing_direction, turn_count



def move_one_step_forward(x_cord,y_cord,x_cord_change,y_cord_change): # moves the guards forward one square based on their current facing direction
    new_x_cord = x_cord + x_cord_change[0]
    new_y_cord = y_cord + y_cord_change[0]

    return new_x_cord,new_y_cord



def set_current_square_to_X(grid,x_cord,y_cord):
    grid[y_cord][x_cord] = "?"
    return grid



def check_next_square(grid,x_cord_change,y_cord_change,start_x_cord,start_y_cord): # checks the next square along the guards path for boxs or the egde of the grid
    new_x_cord = start_x_cord + x_cord_change[0]
    new_y_cord = start_y_cord + y_cord_change[0]

    if new_x_cord < 0 or new_y_cord < 0:
        print("LESS THEN 0")
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
    

    while True: # loops until the guard looks off the grid, then it returns the final grid 

        # values added to the x and y cords to move the guard in their current facing direction 
        x_coord_direction_change = movement_directions[current_facing_direction][1]
        y_coord_direction_change = movement_directions[current_facing_direction][0]
        
        # checks if the next square is empty, a box, or the egde of the grid (returns Ture or False or 0)
        bool_output = check_next_square(main_grid,x_coord_direction_change,y_coord_direction_change,x_coord,y_coord)
        
        # replaces the guards current square with a ?
        set_current_square_to_X(main_grid,x_coord,y_coord)


        if bool_output == -1: # if out of grid bounds: return grid and terminate "main"
            print("out of bounds")
            return main_grid
        

        elif bool_output == False: # if box: turn 90deg right
            print(f"HIT A BOX \nTotal unique moves = {sum(X.count('?') for X in main_grid)}")

            current_facing_direction,turn_count = turn_90_deg_right(turn_count,movement_directions_list)
            continue

        elif bool_output == True: # if empty: move one step fowrard
            print(f"Moving >>> {current_facing_direction}")

            x_coord,y_coord = move_one_step_forward(x_coord,y_coord,x_coord_direction_change,y_coord_direction_change)
            continue



""" ORDER OF OPERATIONS FOR GUARD ALGORITHOM
1: get the guards current x and y cords
2: get current facing direction or CFD

3: change the grid square the guard is on to an "X"
4: check the next grid square in its path based on its CFD

5: turn 90 deg right if the square is a #, update the CFD, repeat steps until the path ahead is not blocked
6: move/update the guards current x and y cords based on CFD and Repeat all stepts above
"""
        

if __name__ == "__main__":

    here = os.path.dirname(__file__)
    with open(f"{here}/../input/input6.txt","r") as file:
        content = file.read()


    facing_directions_list = ["up","right","down","left"]
    movement_directions_dict = {"up":[[-1],[0]],"down":[[1],[0]],"left":[[0],[-1]],"right":[[0],[1]]} # dict format = "Direction": [Y_change][X_change]


    grid = parse_input(content)
    starting_info = get_guard_starting_location(grid)

    final_output_grid = main(grid,starting_info,movement_directions_dict,facing_directions_list)


    text = "FINAL OUTPUT"
    print(text.center(130,"="))

    for row in grid: # prints the final grid row by row
        print("".join(row))

    print(text.center(130,"="))
    print(sum(X.count("?") for X in final_output_grid)) # counts the number of "?" on the grid to dertermin final count of uniqce grids quares travaled by the guard