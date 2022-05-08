# TODO:
#       IMPLEMENT A SCRIPT TO CREATE AN IMAGE
#       OF A MAZE FROM A MATRIX 

import numpy as np
import cv2

# THIS IS THE GRID
# mat = [
#     [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
#     [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
#     [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
#     [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
#     [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
#     [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#     [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
# ]

# for i in mat:
#     for j in range(len(i)):
#         if i[j] == 1:
#             i[j] = 255

# data = np.array(mat, dtype=np.int32)

# data[0, 0] = 128

maze = cv2.imread("./mazes/maze2.png")[:, :, 0]

maze = list(maze)
for i in maze:
    for j in range(len(i)):
        if i[j] > 0:
            i[j] = 255

maze = np.array(maze, dtype=np.int32)

cv2.imwrite("./mazes/tmaze2.png", maze)
print("done")