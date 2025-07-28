
import os


def generate_disk_map(file_input:str) -> list:
    disk_map: list = []
    data_index = 0

    for char_index, character in enumerate(file_input):

        if char_index % 2 == 1: 
            for i in range(int(character)):
                disk_map.append(".")
        
        else:
            for i in range(int(character)):
                disk_map.append(int(data_index))
            data_index += 1

    return disk_map



def move_left_pointer(disk_map:list, current_pointer_poition:int) -> int:
        for pointer_index, item in enumerate(disk_map[current_pointer_poition:]):
            if item == ".":
                # print(pointer_index, item)
                return pointer_index + current_pointer_poition
            continue

def move_right_pointer(disk_map:list, current_pointer_poition:int) -> int:
    for pointer_index in range(current_pointer_poition - 1, -1, -1):

        if disk_map[pointer_index] != ".":
            # print(pointer_index,disk_map[pointer_index])
            return pointer_index



def swap_items_at_pointers(left:int, right:int, disk_map:list) -> list:
    disk_map[left],disk_map[right] = disk_map[right],disk_map[left]

    # print(f"SWAPED {disk_map[left]} AND {disk_map[right]}")
    return disk_map




def reorder_disk_map(disk_map:list) -> list:
    left_pointer = 0
    right_pointer = int(len(disk_map))

    while True:
            left_pointer = move_left_pointer(disk_map,left_pointer)
            right_pointer = move_right_pointer(disk_map,right_pointer)

            if left_pointer > right_pointer:
                del disk_map[right_pointer + 1:]
                return disk_map

            disk_map = swap_items_at_pointers(left_pointer,right_pointer,disk_map)
    

def calculate_check_sum(disk_map):
    total_check_sum = 0
    for index, item in enumerate(disk_map):
        total_check_sum += index * item
    print(f'TOTAL CHECKSUM = {total_check_sum}')



def main(content):
    disk_map = generate_disk_map(file_input=content)
    print(f"\nINPUT = {disk_map}")

    reordered_disk_map = reorder_disk_map(disk_map)
    print(f"OUTPUT = {reordered_disk_map}\n---------------------")

    calculate_check_sum(reordered_disk_map)
    

if __name__ == "__main__":
    here = os.path.dirname(__file__)
    with open(f"{here}/../input/sample9.txt","r") as file:
        content = file.read()

    main(content)
   