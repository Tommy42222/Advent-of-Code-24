import os,sys


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





if __name__ == "__main__":
    here = os.path.dirname(__file__)
    with open("../input/sample9.txt","r") as file:
        content = file.read()

    disk_map = generate_disk_map(content)
    print(disk_map)