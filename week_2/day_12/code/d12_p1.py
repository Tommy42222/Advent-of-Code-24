import os,time
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

def parse_input(input:str) -> list[str]:
    return [list(line) for line in input.splitlines()]


def fill_search(x_cord: int, y_cord: int, grid:list[str], visted:set, plant_area:int, perimeter:int, plant_token:str):
        x_change = [0,0,1,-1]
        y_change = [1,-1,0,0]
        try:

            if grid[y_cord][x_cord] != plant_token or x_cord < 0 or y_cord < 0: # if current square is not of the same plant type, 
                perimeter += 1
                return visted, plant_area, perimeter 

            elif (y_cord,x_cord) in visted:
                pass
            
            else:
                plant_area += 1
                visted.add((y_cord,x_cord))
                for i in range(4):
                    visted, plant_area, perimeter = fill_search(x_cord+x_change[i],y_cord+y_change[i],grid,visted,plant_area,perimeter,plant_token) 
             
        except IndexError:
            perimeter += 1
        
        # print(f"out: {visted =} {plant_area = } {perimeter = }")
        return visted, plant_area, perimeter 


def main():
    content = read_file("i",12)
    _input_grid:list = parse_input(content)
    visted = set()
    total_cost:int = 0

    for row_index, row in enumerate(_input_grid):
        for item_index, item in enumerate(row):
            
            coordinates = (row_index,item_index)

            if coordinates not in visted:
                # run fill function
                plant_area = 0
                perimeter = 0
                plant_token = _input_grid[row_index][item_index]
                
                visted, plant_area, perimeter = fill_search(item_index,row_index,_input_grid,visted,plant_area,perimeter,plant_token) 

                total_cost += (plant_area * perimeter)
                print(f"Flowe Type = {plant_token}, {plant_area = }, {perimeter = }, cost = £{perimeter * plant_area}")

    print(f"TOTAL COST = £{total_cost:,}")


if __name__ == "__main__":
    a = time.time()
    main()
    b = time.time()

print(f"total run time = {b - a:.2f}s")