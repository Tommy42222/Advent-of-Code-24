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



def find_blank(_content) -> int:
    for index,item in enumerate(_content):
        if item == "":
            return index



def parse_input(_content:list) -> tuple[list[str],str]:
    id = find_blank(_content)
    
    area_map:list = [list(line) for index,line in enumerate(_content) if index < id]
    instructions = "".join([(line) for index,line in enumerate(_content) if index > id])

    return area_map,instructions

def print_area_map(area_map:str, seperator:str):
    for row in area_map:
        print(seperator.join(row))

def generate_wider_map(area_map:list[str]) -> list[str]:
    new_map = []
    for row in area_map:
        row_list:list = []
        for item in row:

            match item:
                case "#":
                    new_item_L = "#"
                    new_item_R = "#"
                case "O":
                    new_item_L = "["
                    new_item_R = "]" 
                case ".":
                    new_item_L = "."
                    new_item_R = "." 
                case "@":
                    new_item_L = "@"
                    new_item_R = "."
                
            row_list.append(new_item_L)
            row_list.append(new_item_R)

        new_map.append(row_list)



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
        case ".": # empty space
            output = "moving"
            bot_postion = next_square_position


        case "]" | "[" : # box
            can_be_pushed:bool = None
            output = "pushing box"
            box_chain_corrdinates = []

            if movement_vector.vy != 0:
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
            pass
    
    # print(f"{bot_postion.py,bot_postion.px}")
    # print(output)
    area_map[bot_postion.py][bot_postion.px] = "@" # place the robot on the new square
    return area_map, bot_postion



def push_box_verticaly(area_map:list[str],box_location:namedtuple,box_token:str, vectors:namedtuple,box_chain_corrdinates:list) -> tuple[bool,list[tuple[int,int]]]:
    Coordinates = namedtuple("Coordinates",("py","px"))
    temp = set(chain(*chain(i for i in box_chain_corrdinates)))
    # print(f"{box_token = }")

    if ((box_location.py,box_location.px) in temp) or ((box_location.px,box_location.py) in box_chain_corrdinates):
        return True, box_chain_corrdinates

    if box_token == "]":
        l_check = Coordinates(box_location.py + vectors.vy,box_location.px - 1)
        r_check = Coordinates(box_location.py + vectors.vy,box_location.px)
        box_chain_corrdinates.append([(box_location.py,box_location.px),(box_location.py,box_location.px -1)])


    elif box_token == "[":
        l_check = Coordinates(box_location.py + vectors.vy,box_location.px)
        r_check = Coordinates(box_location.py + vectors.vy, box_location.px + 1)
        box_chain_corrdinates.append([(box_location.py,box_location.px),(box_location.py,box_location.px + 1)])


    elif box_token == ".":
        return True, box_chain_corrdinates
    
    else:
        print("somethings has gone fucking WRONG")


    l_check_sqaure = area_map[l_check.py][l_check.px]
    r_check_square = area_map[r_check.py][r_check.px]
    
    if l_check_sqaure == "[" and r_check_square == "]":
        output_bool,box_chain_corrdinates = push_box_verticaly(area_map=area_map,box_location=l_check,box_token=l_check_sqaure,vectors=vectors,box_chain_corrdinates=box_chain_corrdinates)

    elif l_check_sqaure == "." and r_check_square == ".":
        return True, box_chain_corrdinates
    
    elif l_check_sqaure == "#" or r_check_square == "#":
        return False,box_chain_corrdinates

    elif l_check_sqaure == "]" or r_check_square == "[":
            output_a,box_chain_corrdinates = push_box_verticaly(area_map=area_map,box_location=l_check,box_token=l_check_sqaure,vectors=vectors,box_chain_corrdinates=box_chain_corrdinates)
            output_b,box_chain_corrdinates = push_box_verticaly(area_map=area_map,box_location=r_check,box_token=r_check_square,vectors=vectors,box_chain_corrdinates=box_chain_corrdinates)
            
            if output_a == False or output_b == False:
                return False, box_chain_corrdinates 
            else:
                return True, box_chain_corrdinates
    

    return output_bool, box_chain_corrdinates



def push_box_horizontally(area_map:list[str],box_location:namedtuple,box_token:str, vectors:namedtuple, box_chain_corrdinates:list) -> tuple[bool,list[tuple[int,int]]]:
    Coordinates = namedtuple("Coordinates",("py","px"))

    current_square = box_token
    dx = box_location.px
    dy = box_location.py

    while current_square != "#":
        box_chain_corrdinates.append((Coordinates(dy,dx),Coordinates(dy,dx + vectors.vx)))
        
        dx = dx + (vectors.vx * 2)

        current_square = area_map[dy][dx]
        if current_square == ".":
            return True, box_chain_corrdinates
    
    return False, box_chain_corrdinates


def update_boxes(area_map:list[str],box_chain_corrdinates:list[tuple[int,int],tuple[int,int]],vectors:namedtuple,robot_position:namedtuple):
    Coordinates = namedtuple("Coordinates",("py","px"))
    # clear the boxes off the grid
    for box in box_chain_corrdinates:
        for sub_box in box:
            y = sub_box[0]
            x = sub_box[1]
            area_map[y][x] = "."
    # add the moved boxes to the grid
    for new_box in box_chain_corrdinates:
        boxes = ["[","]"]
        if new_box[0][1] > new_box[1][1]:
            boxes = ["]","["]

        for id, sub_box in enumerate(new_box):
            y = sub_box[0]
            x = sub_box[1]
            area_map[y+vectors.vy][x+vectors.vx] = boxes[id]

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
    print_area_map(area_map,"")

    # gets the coordinates to start the program from
    bot_postion:namedtuple[int,int] = get_bot_starting_position(area_map)

    
    # for each command in the instructons
    for direction in instructions:
        directional_vector = direction_values[direction]
        area_map,bot_postion = move_bot(area_map,directional_vector,bot_postion) # main function
        print(direction, end=" ")

    final_checksum = calculate_checksum(area_map)
    print_area_map(area_map,"")
    print(f"{final_checksum =:,}")


if __name__ == "__main__":
    s = time.time() # timer start
    main() 
    f = time.time() # timer end
    print(f"TOTAL RUN TIME = {f-s:.3f}s") # prints total run time in seconds