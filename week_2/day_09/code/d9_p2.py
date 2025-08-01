import os,time


def generate_disk_map(file_input:str) -> list| dict| dict:
    disk_map = []
    empty_space = {}       # FORMAT: [start_index]: length_of_empty_space
    data_block_info = {}   # FORMAT: [(data_index)]: (start_index, length_of_data_block)
                           # all keys and items in both dicts are ints

    data_block_index = 0
    disk_map_length = 0

    for char_index, character in enumerate(file_input):

        if character == "0":
            # print("0 value found")
            continue
        

        if file_input[char_index-1] == "0" and char_index % 2 == 1:
            last_key = list(empty_space.keys())[-1]
            empty_space[last_key] += int(character)

            for i in range(int(character)):
                disk_map.append(".")
            continue


        if char_index % 2 == 0:

            data_block_info[data_block_index] = (disk_map_length,int(character))
            for i in range(int(character)):
                disk_map.append(int(data_block_index))

            data_block_index += 1


        else:
            empty_space[disk_map_length] = int(character)
            for i in range(int(character)):
                disk_map.append(".")

        disk_map_length += int(character)


    # print("DB",data_block_info)
    # print("ES",empty_space)
    # print("DM",disk_map)
    return disk_map,empty_space,data_block_info






def swap_items_at_pointers(left:int, right:int,iteration_count:int, disk_map:list) -> list:
    for iteration in range(iteration_count):

        disk_map[left],disk_map[right] = disk_map[right],disk_map[left]
        # print(f"SWAPED {disk_map[right]} ID = {left}| AND {disk_map[left]} ID = {right}")

        left += 1
        right += 1

    # print(disk_map,"+")
    return disk_map




def reorder_disk_map(disk_map:list, empty_space_info:dict, data_info:dict) -> list:

    for item in list(reversed(data_info.items())):
        output, empty_space_info  = search_disk_for_space(item,empty_space_info)
       
        if output == None:
            continue

        # print("-----")
        swap_items_at_pointers(output[0],output[1],iteration_count=output[2],disk_map=disk_map)

    return disk_map

def shrink_empty_space_dict(empty_space_info:dict, key: int, data_width:int):
    # print(empty_space_info)

    value = empty_space_info.pop(key)  # Pop only the value, we already know the key

    new_key = key + data_width
    new_value = value - data_width
    
    if new_value == 0:
        return empty_space_info
    
    empty_space_info[new_key] = new_value
    sorted_dict = dict(sorted(empty_space_info.items()))

    # print(f"{data_width = } {new_key = } {new_value = }")
    # print(sorted_dict)
    return sorted_dict



def search_disk_for_space(data_block, empty_space_info:dict):
    data_width = data_block[1][1]
    data_location = data_block[1][0]

    # print(f"input_{data_block[0]}, locaiton = {data_location}, WIDTH = {data_width}")

    for space in empty_space_info.items():

        space_locaton = space[0]
        space_width = space[1]


        if space_locaton > data_location:
            # print("space found to the right of data")
            break
        
        elif space_width >= data_width:
            output =  (data_location,space_locaton,data_width)

            # print(f"VALID GAP FOUND AT location = {space_locaton}, WIDTH = {space_width}")
            empty_space_info = shrink_empty_space_dict(empty_space_info,space_locaton,data_width)

            # print(output)
            return output,empty_space_info


        else:
            # print("no fit")
            pass

    return None,empty_space_info




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

    # for char in reordered_disk_map:
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
    