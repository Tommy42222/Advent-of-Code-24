import os,time
from pprint import pprint
from collections import namedtuple
from itertools import chain



def read_file(option:str, day_number:int) -> str:
    here = os.path.dirname(__file__)
    content = "ERROR WHEN READING FILE "
    
    if option == "i":
        with open(f"{here}/../input/input{day_number}.txt", "r") as file:
            content = file.read()

    elif option == "s":
        with open(f"{here}/../input/sample{day_number}.txt", "r") as file:
            content = file.read()
    else:
        raise ValueError(f"Input must be either 's' or 'i'... You entered '{option}' <<< shame on you...")

    return content



def find_blank_line(_content) -> int:
    for index,item in enumerate(_content):
        if item == "":
            return index



def parse_input(_content:list) -> tuple[list[str],str]:
    id = find_blank_line(_content)
    
    area_map:list = [list(line) for index,line in enumerate(_content) if index < id]
    instructions = "".join([(line) for index,line in enumerate(_content) if index > id])

    return area_map,instructions



def output_area_map(area_map:str, seperator:str): # outputs the area map as a string instead of list
    for row in area_map:
        print(seperator.join(row))



def generate_wider_map(area_map:list[str]) -> list[str]:
    new_map = [] # final list
    for row in area_map:
        row_list:list = [] # for each row
        for item in row:    
            match item:
                case "#":
                    items = ["#","#"]
                case "O":
                    items = ["[","]"]
                case ".":
                    items = [".","."]
                case "@":
                    items = ["@","."]
            
            row_list.extend(items) # items are added to the end of "row_list"
        new_map.append(row_list) # row is added to final list

    return new_map


def get_bot_starting_position(area_map:list) -> tuple[int,int]:
    Coordinates = namedtuple("Coordinates",("py","px"))
    for row_index, row in enumerate(area_map):
        for item_index, item in enumerate(row):
            if item == "@":
                return Coordinates(row_index,item_index)



def move_bot(area_map:list[str],movement_vector:namedtuple, bot_postion:namedtuple) -> tuple[list[str],namedtuple]:
    Coordinates = namedtuple("Coordinates",("py","px"))
    area_map[bot_postion.py][bot_postion.px] = "." # repace the robot with a "."

    dx = bot_postion.px + movement_vector.vx
    dy = bot_postion.py + movement_vector.vy
    
    next_square = area_map[dy][dx]
    next_square_position = Coordinates(dy,dx)

    output = "8=====* <<<"
    # print(f"{next_square = } | {bot_postion.py,bot_postion.px} ->" ,end=" ")

    match next_square: # main logic based on what next_sqaure is

        case ".": # if empty space
            output = "moving"
            bot_postion = next_square_position


        case "[" | "]" : # if box
            box_chain_corrdinates:list[tuple[int,int],tuple[int,int]] = [] # stores each coordinate pair for each "[" and "]". This is used to visualy update the boxes position after they have been pushed.
            can_be_pushed:bool = None
            
            output = "pushing box"

            if movement_vector.vy != 0: # if vector Y == 0, then the bot is moving horizontaly
                output = "verticaly"
                can_be_pushed ,box_chain_corrdinates = push_box_verticaly(area_map=area_map,box_location=next_square_position,box_token=next_square,vectors=movement_vector,box_chain_corrdinates=box_chain_corrdinates)

                if can_be_pushed == True:
                    area_map,bot_postion = update_boxes(area_map=area_map,box_chain_corrdinates=box_chain_corrdinates,vectors=movement_vector,robot_position=bot_postion)
            
            else:
                output = "horizontaly"
                can_be_pushed, box_chain_corrdinates = push_box_horizontally(area_map=area_map,box_location=next_square_position,box_token=next_square,vectors=movement_vector,box_chain_corrdinates=box_chain_corrdinates)

                if can_be_pushed == True:
                    area_map,bot_postion = update_boxes(area_map=area_map,box_chain_corrdinates=box_chain_corrdinates,vectors=movement_vector,robot_position=bot_postion)


        case "#": # wall
            output = "hit a wall"

    
    print(f"{bot_postion.py,bot_postion.px}",end="| ")
    print(output)
    area_map[bot_postion.py][bot_postion.px] = "@" # place the robot on the new square
    return area_map, bot_postion



def push_box_verticaly(area_map:list[str],box_location:namedtuple,box_token:str, vectors:namedtuple,box_chain_corrdinates:list) -> tuple[bool,list[tuple[int,int]]]:
    Coordinates = namedtuple("Coordinates",("py","px"))

    temp = set(chain(*chain(i for i in box_chain_corrdinates))) # flattens the list of lists of tuples into a 1d list

    if ((box_location.py,box_location.px) in temp) or ((box_location.px,box_location.py) in box_chain_corrdinates): # check if box has already been visited
        return True, box_chain_corrdinates

    if box_token == "]": # if function is called on the right side of the box.
        # gets the coordinates of the square directly above where the function was called from, and the square to its left
        l_check = Coordinates(box_location.py + vectors.vy,box_location.px - 1)
        r_check = Coordinates(box_location.py + vectors.vy,box_location.px)
        # adds the coordinates of the current box to box_chain_corrdinates
        box_chain_corrdinates.append([(box_location.py,box_location.px),(box_location.py,box_location.px -1)])


    elif box_token == "[": # if function is called on the left side of the box.        
        # gets the coordinates of the square directly above where the function was called from, and the square to its right
        l_check = Coordinates(box_location.py + vectors.vy,box_location.px) 
        r_check = Coordinates(box_location.py + vectors.vy, box_location.px + 1)
        # adds the coordinates of the current box to box_chain_corrdinates
        box_chain_corrdinates.append([(box_location.py,box_location.px),(box_location.py,box_location.px + 1)])


    elif box_token == ".": 
        return True, box_chain_corrdinates
    
    else:
        print("somethings has gone fucking WRONG")


    # gets both squares above the current box
    l_check_sqaure = area_map[l_check.py][l_check.px]
    r_check_square = area_map[r_check.py][r_check.px]
    
    if l_check_sqaure == "[" and r_check_square == "]": # if a box is directly above the current box
        output_bool,box_chain_corrdinates = push_box_verticaly(area_map=area_map,box_location=l_check,box_token=l_check_sqaure,vectors=vectors,box_chain_corrdinates=box_chain_corrdinates)

    elif l_check_sqaure == "." and r_check_square == ".": # if both sqaures directly above the current box are empty space, then the box can be pushed
        return True, box_chain_corrdinates
    
    elif l_check_sqaure == "#" or r_check_square == "#": # if there is a piller/wall directly above the current box, then the NO boxes can be pushed
        return False,box_chain_corrdinates

    elif l_check_sqaure == "]" or r_check_square == "[": # if there is one or more boxes above
            bool_output_A,box_chain_corrdinates = push_box_verticaly(area_map=area_map,box_location=l_check,box_token=l_check_sqaure,vectors=vectors,box_chain_corrdinates=box_chain_corrdinates)
            bool_output_B,box_chain_corrdinates = push_box_verticaly(area_map=area_map,box_location=r_check,box_token=r_check_square,vectors=vectors,box_chain_corrdinates=box_chain_corrdinates)
            
            if bool_output_A == False or bool_output_B == False: # if either box can't be pushed then no boxes can be pushed
                return False, box_chain_corrdinates 
            else:
                return True, box_chain_corrdinates
    

    return output_bool, box_chain_corrdinates



def push_box_horizontally(area_map:list[str],box_location:namedtuple,box_token:str, vectors:namedtuple, box_chain_corrdinates:list) -> tuple[bool,list[tuple[int,int]]]:
    Coordinates = namedtuple("Coordinates",("py","px"))

    current_square = box_token
    dx = box_location.px
    dy = box_location.py

    while current_square != "#": # keep checking square in current facing direction until it either finds empty space "." or hits a wall "#".
        box_chain_corrdinates.append((Coordinates(dy,dx),Coordinates(dy,dx + vectors.vx)))
        
        dx = dx + (vectors.vx * 2) # jump to the next avaliable square in that direction
        current_square = area_map[dy][dx]

        if current_square == ".": 
            return True, box_chain_corrdinates
    
    return False, box_chain_corrdinates



def update_boxes(area_map:list[str],box_chain_corrdinates:list[tuple[int,int],tuple[int,int]],vectors:namedtuple,robot_position:namedtuple):
    Coordinates = namedtuple("Coordinates",("py","px"))
    
    # clear the boxes off the grid
    for box_coords in box_chain_corrdinates:
        for box_edge_coords in box_coords:
            y = box_edge_coords[0]
            x = box_edge_coords[1]
            area_map[y][x] = "."

    # add the moved boxes back to the grid in their new position
    for new_box_coords in box_chain_corrdinates:
        boxes = ["[","]"]

        # flips the order the box is generated
        if new_box_coords[0][1] > new_box_coords[1][1]: 
            boxes = ["]","["]

        for i, box_edge_coords in enumerate(new_box_coords):
            y = box_edge_coords[0]
            x = box_edge_coords[1]
            area_map[y+vectors.vy][x+vectors.vx] = boxes[i]

    # updates the robots postion
    new_robot_position = Coordinates(robot_position.py + vectors.vy,robot_position.px+ vectors.vx)
    return area_map, new_robot_position



def calculate_checksum(area_map:list[str]) -> int:
    checksum = 0
    for row_index, row in enumerate(area_map):
        for item_index, item in enumerate(row):
            if item == "[":
                checksum += 100 * row_index + item_index
                # print(checksum)
    return checksum



def main()-> None:
    final_checksum = 0
    _content = read_file("i","15").splitlines()
 
    # each namedtuple is formated (y-cord,x-cord)
    Vector = namedtuple("Vectors",("vy","vx"))
    direction_values: dict[str:tuple[int,int]] = {"^":Vector(-1,0), ">":Vector(0,1), "v":Vector(1,0), "<":Vector(0,-1)}

    # parse input 
    area_map, instructions = parse_input(_content)
    area_map = generate_wider_map(area_map)

    # outputs the before area map
    output_area_map(area_map,"")

    # gets the coordinates to start the program from
    bot_postion:namedtuple[int,int] = get_bot_starting_position(area_map)


    # for each command in the instructons
    for direction in instructions:
        directional_vector = direction_values[direction]
        area_map,bot_postion = move_bot(area_map,directional_vector,bot_postion) # main function
        print(direction, end=" ")


    final_checksum = calculate_checksum(area_map)
    # print_area_map(area_map,"")
    print(f"{final_checksum =:,}")


if __name__ == "__main__":
    s = time.time() # timer start
    main() 
    f = time.time() # timer end
    print(f"TOTAL RUN TIME = {f-s:.3f}s") # prints total run time in seconds