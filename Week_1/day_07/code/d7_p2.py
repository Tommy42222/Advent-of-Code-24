import os


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

        # print("--------------------------------")
        # print(current_sum,target,values)

        if can_make_target(current_sum,target,values,loop_index,symbol="start") == True:
            final_counter += target
        else:
            print("NO MATCHS", f"{target:,}")
    
    return final_counter


        

def can_make_target(current_sum,target,values_list,index,symbol):
    global iteration_count
    iteration_count += 1
    current_sum = int(current_sum)

    # print(symbol)
    if index == len(values_list):
        if current_sum == target:
            print("MATCH",f"{current_sum:,}")
            return True
        else:
            # print("going backwards",current_sum)
            return False
    else:
        
        return (can_make_target(current_sum + values_list[index],target,values_list,index + 1,symbol=f"+ {current_sum, values_list[index]}") 
                or can_make_target(current_sum * values_list[index],target,values_list,index + 1,symbol=f"* {current_sum, values_list[index]}")
                or can_make_target(str(current_sum) + str(values_list[index]), target,values_list,index + 1, symbol= f"|| {str(current_sum) + str(values_list[index])}"))




if __name__ == "__main__":
    iteration_count = 0
    here = os.path.dirname(__file__)
    with open (f"{here}/../input/input7.txt", "r") as file:
        content = file.read()

    input_values = parse_input_file(content)

    final_sum = main(input_values)

    print(f"-------------------------------*\nFINAL SUM = {final_sum:,}")
    print(f"TOTAL ITERATIONS = {iteration_count:,}")