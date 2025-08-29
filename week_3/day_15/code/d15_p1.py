import os
from pprint import pprint


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
    
    area_map:list = [(line) for index,line in enumerate(_content) if index < id]
    instructions = "".join([(line) for index,line in enumerate(_content) if index > id])

    # pprint(area_map)
    # print(instructions)

    return area_map,instructions







def main()-> None:
    _content = read_file("s","15").splitlines()
    area_map, instructions = parse_input(_content)
    direction_values: dict[str:tuple[int,int]]


if __name__ == "__main__":
    main()