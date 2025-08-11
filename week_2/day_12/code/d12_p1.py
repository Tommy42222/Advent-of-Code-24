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



def fill_search(x_cord: int, y_cord: int, grid:list[str], visted:set, plant_area:int, perimeter:int, plant_token:str) -> tuple[set,int,int]:
        x_change = [0,0,1,-1]
        y_change = [1,-1,0,0]
        try:

            if grid[y_cord][x_cord] != plant_token or x_cord < 0 or y_cord < 0: # if current square is not of the same plant type or includes a negetive index, then an egde has been found
                perimeter += 1
                pass

            elif (y_cord,x_cord) not in visted: # if the current square has already been checked # if current square is valid and of the same type, recursively check the 4 squares around it and add their outputs to visted, plant_area, perimeter
                plant_area += 1
                visted.add((y_cord,x_cord))
                for i in range(4):
                    visted, plant_area, perimeter = fill_search(x_cord+x_change[i],y_cord+y_change[i],grid,visted,plant_area,perimeter,plant_token) 
             
            else:
                pass 
               
        except IndexError: # if a square is out of bounds then an egde has been found
            perimeter += 1
        
        return visted, plant_area, perimeter  


def main():
    _content = read_file("i",12)
    _input_grid:list = parse_input(_content)
    visted = set() 
    total_cost:int = 0 

    for row_index, row in enumerate(_input_grid):
        for item_index, item in enumerate(row):
            item_coordinates:tuple = (row_index,item_index)

            if item_coordinates not in visted: # don't start searching from a sqaure that has already been searched before 
                plant_area:int = 0
                perimeter:int = 0
                plant_token:str = _input_grid[row_index][item_index]
                
                visted, plant_area, perimeter = fill_search(item_index,row_index,_input_grid,visted,plant_area,perimeter,plant_token) 

                total_cost += (plant_area * perimeter)
                print(f"Flowe Type = {plant_token}, {plant_area = }, {perimeter = }, cost = £{perimeter * plant_area}")

    print(f"TOTAL COST = £{total_cost:,}")


if __name__ == "__main__":
    a = time.time()
    main()
    b = time.time()

print(f"total run time = {b - a:.3f}s")