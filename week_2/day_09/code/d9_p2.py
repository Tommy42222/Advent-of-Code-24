import os,time



def generate_disk_map(file_input:str) -> list| dict| dict:
                           # all keys and items in both dicts are ints
    empty_space = {}       # FORMAT: [start_index]: length_of_empty_space
    data_block_info = {}   # FORMAT: [(data_block_ID)]: (start_index, length_of_data_block)
                          
    data_block_index = 0
    disk_map = []

    for char_index, token_value in enumerate(file_input):
        new_token_starting_position = len(disk_map)
        
        if token_value == "0": # skip empty values
            continue
        
        """ - This if statment checks if the n-1 input character was a length 0 datablock (example: 1203)
              if one is detected, combine the gap before and after it into on value in the 'empty_space' dict
            - This ensurse the program can accurate evaluate whever a data block can fit into any given gap. """
        if file_input[char_index-1] == "0" and char_index % 2 == 1:
            last_key = list(empty_space.keys())[-1]
            empty_space[last_key] += int(token_value)

            for i in range(int(token_value)):
                disk_map.append(".")
            continue


        if char_index % 2 == 0: # for adding data blocks

            data_block_info[data_block_index] = (new_token_starting_position,int(token_value))
            for i in range(int(token_value)):
                disk_map.append(int(data_block_index))

            data_block_index += 1


        else: # for adding empty space
            empty_space[new_token_starting_position] = int(token_value)
            for i in range(int(token_value)):
                disk_map.append(".")


    # print("DB",data_block_info)
    # print("ES",empty_space)
    # print("DM",disk_map)
    return disk_map,empty_space,data_block_info



def swap_items_at_pointers(left:int, right:int,block_width:int, disk_map:list) -> list:
    for i in range(block_width):

        disk_map[left],disk_map[right] = disk_map[right],disk_map[left]
        left += 1
        right += 1

    return disk_map



def reorder_disk_map(disk_map:list, empty_space_info:dict, data_info:dict) -> list:
    for item in list(reversed(data_info.items())):
        output, empty_space_info  = search_disk_for_space(item,empty_space_info)
       
        if output == None: # if no valid gaps are found, move on to next data block
            continue
            
        empty_space = output[0]
        data_block = output[1]
        data_block_width = output[2]

        swap_items_at_pointers(left=empty_space,right=data_block,block_width=data_block_width,disk_map=disk_map)
    return disk_map



def shrink_empty_space_dict(empty_space_info:dict, key: int, gap_width:int): #updates the empty_space_info as spaces are filled, so blocks are not placed in already taken spots.

    current_block_width = empty_space_info.pop(key)  
    new_start_index = key + gap_width
    new_gap_width = current_block_width - gap_width
    
    if new_gap_width == 0: # if a gap has a width of 0 return new list without appending new values
        return empty_space_info
    
    empty_space_info[new_start_index] = new_gap_width
    sorted_dict = dict(sorted(empty_space_info.items()))

    return sorted_dict



# This function uses the data in "data_block_info and empty_space_info" to evaluate if there is any gaps to the left of a data block that can fit in it.
def search_disk_for_space(data_block, empty_space_info:dict):

    # unpacks the data for the given data block
    data_width = data_block[1][1]
    data_location = data_block[1][0]

    for gap in empty_space_info.items(): # for every avaliable gap...

        space_locaton = gap[0]
        space_width = gap[1]

        if space_locaton > data_location: # if no gaps are found to the right of the data block
            return None,empty_space_info
        
        elif space_width >= data_width: # if there is a valid gap
            output =  (data_location,space_locaton,data_width)
        
            empty_space_info = shrink_empty_space_dict(empty_space_info,space_locaton,data_width) # update the empty_space_info dict 
            return output,empty_space_info



def calculate_check_sum(disk_map):
    total_check_sum = 0
    for index, item in enumerate(disk_map):
        if item == ".":
            continue

        total_check_sum += index * item
    return total_check_sum



def main(content:str) -> None:

    disk_map,empty_space_dict,data_info_dict = generate_disk_map(file_input=content)
    # print(f"\nINPUT = {disk_map}")

    reordered_disk_map = reorder_disk_map(disk_map,empty_space_dict,data_info_dict)
    print(f"OUTPUT = {reordered_disk_map}\n---------------------")

    striped_disk_maps = [item for item in reordered_disk_map if item != "."]
    # print(striped_disk_maps)

    final_checksum = calculate_check_sum(reordered_disk_map)
    print(f'TOTAL CHECKSUM = {final_checksum:,}')

    # for char in striped_disk_maps:
    #     print(char,end="_")



if __name__ == "__main__":
    here = os.path.dirname(__file__)
    with open(f"{here}/../input/input9.txt","r") as file:
        content = file.read()

    print("PROGRAM RUNNING...")
    start = time.time()
    main(content)
    end = time.time()

    print(f"PROGRAM FINISHED!!\nTOTAL RUN TIME ={end-start:.2f}s")
    