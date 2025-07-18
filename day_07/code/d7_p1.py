import os,pprint,sys
sys.setrecursionlimit(15000)

def parse_input_file(file):
    master_dict = {}
    split_file = file.splitlines()

    for row in split_file:
        values = row.split(":")
        target, equation_values = int(values[0]), [int(item) for item in values[1].split()]
        master_dict[target] = equation_values
        print(target,equation_values)

    return master_dict


def main(content):
    final_counter = 0

    for target,values in content.items():

        current_sum = values[0]
        loop_index = 1

        print("--------------------------------")
        print(current_sum,target,values)

        if can_make_target(current_sum,target,values,loop_index,symbol="start") == True:
            final_counter += target
        else:
            print("NO MATCHS")
    
    return final_counter

        

def can_make_target(current_sum,target,values_list,index,symbol):
    # print(symbol)
    if index == len(values_list):
        if current_sum == target:
            print("MATCH",current_sum)
            return True
        else:
            # print("going backwards",current_sum)
            return False
    else:
        
        return (can_make_target(current_sum + values_list[index],target,values_list,index + 1,symbol=f"+ {current_sum, values_list[index]}") 
                or can_make_target(current_sum * values_list[index],target,values_list,index + 1,symbol=f"* {current_sum, values_list[index]}"))




if __name__ == "__main__":

    here = os.path.dirname(__file__)
    with open (f"{here}/../input/input7.txt", "r") as file:
        content = file.read()

    input_values = parse_input_file(content)

    final_count = main(input_values)

    print(final_count)