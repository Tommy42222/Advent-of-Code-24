import os,time
from collections import defaultdict
from decimal import Decimal

def parse_input(input_str:str) -> list[str]:
    return [number for number in input_str.strip("\n").split()]


def strip_leading_0s(input:str) -> str:
    value = input.lstrip("0")

    if value == "":
        value = "0"

    return value


def perform_operation(item:str) -> list[str]:

    if item == "0":
        return ["1"]
        
    elif len(str(item)) % 2 == 0:
        half_item_length = len(str(item)) // 2
        return [item[0:half_item_length], strip_leading_0s(item[half_item_length:])]
        
    else:
        return [str(int(item) * 2024)]
        

def blink(_input:dict,num_blinks:int):

    if num_blinks == 0:
        return _input

    dd = defaultdict(int)

    for item, count in _input.items():
        for return_value in perform_operation(item=item):
            dd[return_value] += count
    
    # print(dd)
    return blink(dd,num_blinks=num_blinks-1)


def main() -> None:

    here = os.path.dirname(__file__)
    with open(f"{here}/../input/input11.txt", "r") as file:
        content = file.read()
    
    content:list[str] = parse_input(content)

    dd_input = defaultdict(int)
    for i in content:
        dd_input[i] += 1


    stone_count = blink(dd_input,900)

    sum = 0
    for item,freq in stone_count.items():
        sum += freq
        print(f"{item}, {freq:.5e}")


    print(f"\nfinal stone count = {sum:.5e}")
    print(f"number of unique items = {len(stone_count)}")


    

#-------------------

a = time.time()
main()
b = time.time()

print(f"total run time = {b - a:.2f}s")