import os,pprint

def parce_x_y_input_pairs(content):

    input_content_list = content.splitlines()

    new_content_list = []

    for item in range(len(input_content_list)):
        if input_content_list[item] == "":
            break

        else:
            temp = str(input_content_list[item])
            row = temp.split("|")
            new_content_list.append(row)

    return new_content_list


with open("../input/sample5.txt","r") as file:
    content = file.read()


l = parce_x_y_input_pairs(content)
pprint.pprint(l)



