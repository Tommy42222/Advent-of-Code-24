import os,re
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

def get_position_and_velocity(_input:str) -> dict[tuple[int,int]]:
    robots = {}
    Position = namedtuple("Position",("x","y"))
    Velocity = namedtuple("Velocity",("x","y"))

    regex_pattern = re.compile(r"-*\d+")
    matches = [int(match) for match in re.findall(regex_pattern,_input)]
    
    for i in range(len(matches)// 4):
        position = Position(matches[i],matches[i+1])
        velocity = Velocity(matches[i+2],matches[i+3])
        robots[i+1] = (position,velocity)
        
    # pprint(robots)
    return robots
        

def main()-> None:
    _content = read_file("s","14")
    robots:dict = get_position_and_velocity(_content)
    for robot in robots.values():
        ...



if __name__ == "__main__":
    main()