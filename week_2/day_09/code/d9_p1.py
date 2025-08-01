import os,time


def generate_disk_map(file_input:str) -> list:
    disk_map: list = []
    data_index = 0

    for char_index, character in enumerate(file_input):

        if char_index % 2 == 0: 
            for i in range(int(character)):
                disk_map.append(int(data_index))
            data_index += 1
    
        else:
            for i in range(int(character)):
                disk_map.append(".")
                
    return disk_map



def move_left_pointer(disk_map:list, current_pointer_poition:int) -> int: # when called, jump the L_pointer right to the next empty space "."
        for pointer_index, item in enumerate(disk_map[current_pointer_poition:]):
            if item == ".":
                return pointer_index + current_pointer_poition



def move_right_pointer(disk_map:list, current_pointer_poition:int) -> int: # when called, jump the R_pointer left to the next filled space
    for pointer_index in range(current_pointer_poition - 1, -1, -1): # starts at the -1 index and iterates right to left thorugh the list
        if disk_map[pointer_index] != ".":
            return pointer_index



def swap_items_at_pointers(left:int, right:int, disk_map:list) -> list: 
    disk_map[left],disk_map[right] = disk_map[right],disk_map[left] 

    # print(f"SWAPED {disk_map[left]} AND {disk_map[right]}")
    return disk_map




def reorder_disk_map(disk_map:list) -> list:
    left_pointer = 0                     # start at the beginning of the disk_map
    right_pointer = int(len(disk_map))   # start at the end of the disk_map

    while True:
            left_pointer = move_left_pointer(disk_map,left_pointer)
            right_pointer = move_right_pointer(disk_map,right_pointer)

            if left_pointer > right_pointer:      # the disk is sorted when the two pointers cross each other.
                del disk_map[right_pointer + 1:]  # once sorted, remove all "." after after the r_pointer to save space
                return disk_map
            
            else:
                disk_map = swap_items_at_pointers(left_pointer,right_pointer,disk_map)
    


def calculate_check_sum(disk_map:list) -> int:
    total_check_sum = 0
    for index, item in enumerate(disk_map):
        total_check_sum += index * item
    return total_check_sum



def main(content:str) -> None:
    disk_map = generate_disk_map(file_input=content)
    # print(f"\nINPUT = {disk_map}")

    reordered_disk_map = reorder_disk_map(disk_map)
    # print(f"OUTPUT = {reordered_disk_map}\n---------------------")

    final_checksum = calculate_check_sum(reordered_disk_map)
    print(f'TOTAL CHECKSUM = {final_checksum}')

    



if __name__ == "__main__":
    here = os.path.dirname(__file__)
    with open(f"{here}/../input/input9.txt","r") as file:
        content = file.read()
    
    print("PROGRAM RUNNING...")
    start = time.time()
    main(content)
    end = time.time()

    print(f"PROGRAM FINISHED!!\nTOTAL RUN TIME ={end-start:.2f}s")