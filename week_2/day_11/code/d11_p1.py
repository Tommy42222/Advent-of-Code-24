import os,time


def parse_input(input_str:str) -> list[int]:
    return [int(number) for number in input_str.split(" ")]


class Make_List_Of_Stones:
    def __init__(self,stones,iteration_count) -> None:
        self.stones = stones
        self.iteration_count = iteration_count
        self.index = 0

    def set_index_to_0(self):
        self.index = 0

    def mult_by_2024(self,item_index:int) -> None:
        self.stones[item_index] = int(self.stones[item_index]) * 2024
     

    def change_to_1(self,item_index:int) -> None:
        self.stones[item_index] = 1


    def split_in_half(self,item_index:int) -> None:

        token = str(self.stones[item_index])
        token_length = len(token)

        left_half = int(token[0:token_length//2])
        right_half = int(token[token_length//2:])

        # right_half = right_half.lstrip("0")

        # if right_half == "":
        #     right_half = 0

    
        self.stones[item_index] = left_half
        self.stones.insert(item_index +1,right_half)

        self.index += 1


def main() -> None:

    here = os.path.dirname(__file__)
    with open(f"{here}/../input/input11.txt", "r") as file:
        content = file.read()

    stones = Make_List_Of_Stones(parse_input(content),25)

    for i in range(0,stones.iteration_count):
        stones.set_index_to_0()
        t1 = time.time()
        while True:

            if stones.index == len(stones.stones):
                print(f"after {i + 1} blinks",end=" ")
                t2 = time.time()
                print(f" time to calculate blink = {t2 - t1:.2f}s")
                break
            
            if stones.stones[stones.index] == 0:
                stones.change_to_1(stones.index)

            elif len(str(stones.stones[stones.index])) % 2 == 0:
                stones.split_in_half(stones.index)            

            else:
                stones.mult_by_2024(stones.index)
                    
            stones.index += 1

        
        # print(stones.stones,"\n")
    print(f"final number of stones after {stones.iteration_count} blinks = {len(stones.stones)}")
#-------------------

a = time.time()
main()
b = time.time()

print(f"total run time = {b - a:.2f}s")