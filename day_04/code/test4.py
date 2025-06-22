import numpy as np

lists = np.array(
    [[["x"],["y"],["z"]],
     [["x"],["y"],["z"]],
     [["x"],["y"],["z"]]]
)


if lists[0][0] == "x" and lists[1][1] == "y" and lists[2][2] == "z":
    print("Y")