import os,re
from pprint import pprint
from collections import namedtuple

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

def get_next_machine_input(input_content:list[str]) -> namedtuple :
    Values = namedtuple("Values",("x_value","y_value"))

    text = input_content[:3] # the each machine has three rows: (values for button_A, values for button_B, the target values)
    machine = " ".join(text) # joins the three rows together into single string for easier regex searching
    del input_content[:4] # remove the machine and extra gap from the list


    # regex serach patterns
    x_values_pattern = re.compile(r"X.\d*")
    y_values_pattern = re.compile(r"Y.\d*")

    x_values = re.findall(x_values_pattern,machine)
    y_values = re.findall(y_values_pattern,machine)
    
    # removes the X= and Y= prefix's from each iten in the lists
    x_values = [sub[2:] for sub in x_values]
    y_values = [sub[2:] for sub in y_values]
    
    button_A = Values(x_values[0],y_values[0])
    button_B = Values(x_values[1],y_values[1])
    targets = Values(x_values[2],y_values[2])

    return button_A, button_B, targets, input_content
    

def main() -> None:
    _content = read_file("s","13").splitlines()
    
    while len(_content) > 0: # for each machine in _content
        button_A,button_B,targets,_content = get_next_machine_input(_content)
        
        
        print(button_A,button_B,targets)
        

if __name__ == "__main__":
    main()