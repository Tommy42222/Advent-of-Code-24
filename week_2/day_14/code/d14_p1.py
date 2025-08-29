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
    robots: dict = {}
    Position = namedtuple("Position",("x","y"))
    Velocity = namedtuple("Velocity",("x","y"))

    regex_pattern = re.compile(r"-*\d+")

    for id,machine in enumerate(_input):
        row_matches: list = [int(match) for match in re.findall(regex_pattern,machine)]

        position = Position(row_matches[0],row_matches[1])
        velocity = Velocity(row_matches[2],row_matches[3])
        print(position,velocity)
    
        robots[id] = (position,velocity)
    # pprint(robots)
    return robots



def calcluate_robot_final_position(robot:tuple[tuple[int,int]],num_of_seconds:int, quadrant_map:dict[int],area_width:int, area_height:int) -> dict[int]:
    position = robot[0]
    velocity = robot[1]

    px = position.x
    py = position.y
    
    vx = velocity.x
    vy = velocity.y
    print(f"start = {px} {py}" ,end="| ")
    
    px = (px +(vx * num_of_seconds)) % area_width
    py = (py +(vy * num_of_seconds)) % area_height

    # for seconds in range(num_of_seconds):
    #     # px = (px + vx)
    #     # if px > (area_width-1) or px < 0:
    #     #     px = px % (area_width)

    #     py = (py + vy)
    #     if py > (area_height-1) or py < 0:
    #         py = py % (area_height)


    print(f"end = {px,py}")
    quadrant_map = place_robot_in_quadrant((px,py),quadrant_map,area_width,area_height)
    return quadrant_map



def place_robot_in_quadrant(final_position:tuple[int,int], quadrant_map:dict[int], area_width:int, area_height:int) -> dict[int]:
    if area_height % 2 == 0 and area_width % 2 == 0:
        horizontal_centre = ((area_width + 1) // 2) - 1
        vertical_centre = ((area_height + 1) // 2) -1 
    else:
        horizontal_centre = area_width // 2
        vertical_centre = area_height // 2

    px = final_position[0]
    py = final_position[1]

    if px == horizontal_centre or py == vertical_centre:
        # print("removing non quadrent robot")
        pass

    elif px > horizontal_centre and py > vertical_centre:
        quadrant_map["SE"] += 1

    elif px > horizontal_centre and py < vertical_centre:
        quadrant_map["NE"] += 1
    
    elif px < horizontal_centre and py < vertical_centre:
        quadrant_map["NW"] += 1
    else:
        quadrant_map["SW"] += 1

    return quadrant_map



def calculate_safety_rating(_input:dict) -> int:
    final_product = 1
    for v in _input.values():
        final_product = (final_product * v)
    return final_product



def main()-> None:
    _content = read_file("i","14").splitlines()

    quadrant_map = {"NE":0,"SE":0,"SW":0,"NW":0,}
    robots:dict = get_position_and_velocity(_content)

    for robot in robots.values():
        # print(robot)
    
        quadrant_map:dict = calcluate_robot_final_position(robot=robot,num_of_seconds=100,quadrant_map=quadrant_map,area_width=101,area_height=103)
    safety_rating:int= calculate_safety_rating(quadrant_map)
    print(quadrant_map)
    print(safety_rating)
    

if __name__ == "__main__":
    main()