import os
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



def main():
    content = read_file("s",12)
    _input:list = parse_input(content)
    visted = set()



    pprint(_input)





if __name__ == "__main__":
   main()


