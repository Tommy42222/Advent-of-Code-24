import os,time
from pprint import pprint
from collections import namedtuple



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

    # print(f"{next_square = } | {bot_postion.py,bot_postion.px} ->" ,end=" ")

    match next_square: # main logic based on what next_sqaure is
        case ".": # empty space
            output = "moving"
            bot_postion = next_square_position

        case "O": # box
            output = "pushing box"
            area_map, bot_postion = push_box(area_map=area_map,box_location=next_square_position,robot_position=bot_postion,vectors=movement_vector)

        case "#": # wall
            output = "hit a wall"
            pass
    
    # print(f"{bot_postion.py,bot_postion.px}")
    print(output)
    area_map[bot_postion.py][bot_postion.px] = "@" # place the robot on the new square
    return area_map, bot_postion



def push_box(area_map:list[str],box_location:namedtuple, robot_position:namedtuple, vectors:namedtuple) -> tuple[list[str],namedtuple]:
    """
        - This function searches outwards based on the vector 
        - It keeps searching until it hits a "#"
        - if it finds a "." before a "#"
            - swap the "O" and the "." 
            - move the robot onto the "."
    """
    next_square = "0"
    dx = box_location.px + vectors.vx
    dy = box_location.py + vectors.vy
    while next_square != "#": 

        next_square = area_map[dy][dx]
        if next_square == ".":

            area_map[dy][dx],area_map[box_location.py][box_location.px] = area_map[box_location.py][box_location.px],area_map[dy][dx]
            robot_position = box_location

            return area_map,robot_position

        # add the x,y vectors to the current squares
        dx = dx + vectors.vx
        dy = dy + vectors.vy

    # print("no room to push")
    return area_map,robot_position



def calculate_checksum(area_map:list[str]) -> int:
    checksum = 0
    for row_index, row in enumerate(area_map):
        for item_index, item in enumerate(row):
            if item == "O":
                checksum += 100 * row_index + item_index
                # print(checksum)
    return checksum



def main()-> None:
    _content = read_file("i","15").splitlines()

    # parse input 
    area_map, instructions = parse_input(_content)
    bot_postion:namedtuple[int,int] = get_bot_starting_position(area_map)

    # each namedtuple is formated (y-cord,x-cord)
    Vector = namedtuple("Vectors",("vy","vx"))
    direction_values: dict[str:tuple[int,int]] = {"^":Vector(-1,0), ">":Vector(0,1), "v":Vector(1,0), "<":Vector(0,-1)}
    final_checksum = 0

    # for each command in the instructons
    for command in instructions:
        directional_vector = direction_values[command]
        area_map,bot_postion = move_bot(area_map,directional_vector,bot_postion)


    final_checksum = calculate_checksum(area_map)
    print(f"{final_checksum =:,}")


if __name__ == "__main__":
    s = time.time() # timer start
    main() 
    f = time.time() # timer end
    print(f"TOTAL RUN TIME = {f-s:.3f}s") # prints total run time in seconds