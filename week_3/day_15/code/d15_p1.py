import os
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


def move_bot(area_map:list[str],movement_vector:tuple[int,int], bot_postion:tuple[int,int]) -> tuple[list[str],tuple[int,int]]:
    
    ...


def main()-> None:
    _content = read_file("s","15").splitlines()

    area_map, instructions = parse_input(_content)
    bot_postion:namedtuple[int,int] = get_bot_starting_position(area_map)

    # remove the bot from the area map as to prevent errros if the bot try's and move back onto its starting square
    area_map[bot_postion.py][bot_postion.px] = "."

    # each namedtuple is formated (y-cord,x-cord)
    Vector = namedtuple("Vectors",("vy","vx"))
    direction_values: dict[str:tuple[int,int]] = {"^":Vector(1,0), ">":Vector(0,1), "v":Vector(-1,0), "<":Vector(0,-1), None:Vector(0,0)}

    for command in instructions:

        directional_vector = direction_values[command]
        area_map,bot_postion = move_bot(area_map,directional_vector,bot_postion)
        
        # print(command,end=" ")
        # print((direction_values[command].vy,direction_values[command].vx))
        ...


if __name__ == "__main__":
    main()