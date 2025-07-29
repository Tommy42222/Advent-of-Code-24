import os,time


def generate_disk_map(file_input:str) -> list| dict| dict:
    disk_map = []
    empty_space = {}       # FORMAT: [start_index]: length_of_empty_space
    data_block_info = {}   # FORMAT: [(data_index)]: (start_index, length_of_data_block)
                           # all keys and items in both dicts are ints

    data_block_index = 0
    disk_map_length = 0

    for char_index, character in enumerate(file_input):
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


    print("DB",data_block_info)
    print("ES",empty_space)
    # print("DM",disk_map)
    return disk_map,empty_space,data_block_info






def swap_items_at_pointers(left:int, right:int,iteration_count:int, disk_map:list) -> list:
    for iteration in range(iteration_count):

        disk_map[left],disk_map[right] = disk_map[right],disk_map[left]
        print(f"SWAPED {disk_map[right]} ID = {left}| AND {disk_map[left]} ID = {right}")

        left += 1
        right += 1


    print(disk_map)
    return disk_map




def reorder_disk_map(disk_map:list) -> list:
    left_pointer = 0                     # start at the beginning of the disk_map
    right_pointer = 5   # start at the end of the disk_map
    swap_items_at_pointers(left_pointer,right_pointer,iteration_count=5,disk_map=disk_map)
 


def calculate_check_sum(disk_map):
    total_check_sum = 0
    for index, item in enumerate(disk_map):
        total_check_sum += index * item
    return total_check_sum



def main(content:str) -> None:

    disk_map,empty_dict,data_info_dict = generate_disk_map(file_input="21212121")
    print(f"\nINPUT = {disk_map}")

    reordered_disk_map = reorder_disk_map(disk_map)
    print(f"OUTPUT = {reordered_disk_map}\n---------------------")

    final_checksum = calculate_check_sum(reordered_disk_map)
    print(f'TOTAL CHECKSUM = {final_checksum}')





if __name__ == "__main__":
    here = os.path.dirname(__file__)
    with open(f"{here}/../input/sample9.txt","r") as file:
        content = file.read()

    print("PROGRAM RUNNING...")
    start = time.time()
    main(content)
    end = time.time()

    print(f"PROGRAM FINISHED!!\nTOTAL RUN TIME ={end-start:.2f}s")