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


def count_corners(current_square: tuple[int,int], grid:list[str], current_plant_token:str ,corners_count: int) -> int:
    # up, right, down, left
    adj_checks = [(1,0),(0,1),(-1,0),(0,-1)]
    # up-right, down-right, down-left, up-left
    diag_checks = [(1,1),(-1,1),(-1,-1),(1,-1)]
    # y,x cords
     
    y_cord = current_square[0]
    x_cord = current_square[1]

    grid_width = len(grid[0])
    grid_height = len(grid)

    for i in range(4):
        j = (i + 1) % 4

        west = (y_cord + adj_checks[i][0], x_cord + adj_checks[i][1])
        north = (y_cord + adj_checks[j][0], x_cord + adj_checks[j][1])
        northWest = (y_cord + diag_checks[i][0], x_cord + diag_checks[i][1])

        # print(f"{west = } {north = } {northWest = }", end=" ")

        west = check_square(west,grid,current_plant_token,grid_width,grid_height)
        north = check_square(north,grid,current_plant_token,grid_width,grid_height)
        northWest = check_square(northWest,grid,current_plant_token,grid_width,grid_height)


        if west == False and north == False:
            corners_count += 1
            # print("both false")
                    
        elif west == True and north == True and northWest == False:
            corners_count += 1
            # print("both true and diag false")
        
        else:
            # print("no")
            ...
    
    # print(f"Corners counted for ({y_cord}, {x_cord}): {corners_count}")
    return corners_count


def check_square(coordinates:tuple[int,int], grid:list[str], plant_token:str, grid_width:int, grid_height:int) -> str:

    y_cord = coordinates[0]
    x_cord = coordinates[1]

    if coordinates[0] < 0 or coordinates[0] >= grid_height or coordinates[1] < 0 or coordinates[1] >= grid_width:
        return False
    
    try:
        square = grid[y_cord][x_cord]

        if square == plant_token:
            return True
        
        else:
            return False

    except IndexError:
        return False   
    
def fill_search(x_cord: int, y_cord: int, grid:list[str], visted:set, plant_area:int, num_of_corners:int, plant_token:str) -> tuple[set,int,int]:
        x_change = [0,0,1,-1]
        y_change = [1,-1,0,0]
        try:

            if grid[y_cord][x_cord] != plant_token or x_cord < 0 or y_cord < 0: # if current square is not of the same plant type or includes a negetive index, then an egde has been found
                pass

            elif (y_cord,x_cord) not in visted: # if the current square has already been checked # if current square is valid and of the same type, recursively check the 4 squares around it and add their outputs to visted, plant_area, perimeter
                
                plant_area += 1
                visted.add((y_cord,x_cord))

                for i in range(4):
                    visted, plant_area, num_of_corners = fill_search(x_cord+x_change[i],y_cord+y_change[i],grid,visted,plant_area,num_of_corners,plant_token) 
             
                coords = (y_cord,x_cord)
                num_of_corners += count_corners(coords,grid,plant_token,0)

            else:
                pass 
               
        except IndexError: # if a square is out of bounds then an egde has been found
            ...
        
        return visted, plant_area, num_of_corners  



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
                num_of_corners:int = 0
                plant_token:str = _input_grid[row_index][item_index]
                
                visted, plant_area, num_of_corners = fill_search(item_index,row_index,_input_grid,visted,plant_area,num_of_corners,plant_token) 
                total_cost += (plant_area * num_of_corners)
                # print("================")
                print(f"Flowe Type = {plant_token}, {plant_area = }, {num_of_corners = }, cost = £{num_of_corners * plant_area}")

    print(f"TOTAL COST = £{total_cost:,}")
    print(num_of_corners)


if __name__ == "__main__":
    a = time.time()
    main()
    b = time.time()

print(f"total run time = {b - a:.3f}s")