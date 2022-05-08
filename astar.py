# TODO:
#       IMPLEMENT A STAR ALGORITHM
#       IN ORDER TO IMPLEMENT A STAR TAKE INPUT OF MATRIX
#       START AND END NODE WILL BE THE COORDINATES IN THE MATRIX
#       ESSENTIALLY THE ROWS AND COLUMNS
import numpy as np
import cv2

mazeName = "maze1"
fileType = "png"
maze = cv2.imread(f"./mazes/{mazeName}.{fileType}")[:, :, 0]

bounds = maze.shape

goal = [4,6]
start = [bounds[0]-1, 0]
stlessStart = [bounds[0]-1, 0]

path = []
visited = [] # will contain tuples of traversed coordinates

x = 0
y = 1

def distance(coords, goal):
    '''
        Returns distance between a node and the goal node
    '''
    euDist = ((coords[x]-goal[x])**2 + (coords[y]-goal[y])**2)**0.5
    return euDist

def moveGen(coords, bounds):
    '''
        Returns a list of possible blocks to move to
    '''
    gen = []
    moves = [
       [1,0],
       [-1,0],
       [0,1],
       [0,-1]
    ]
    for i in range(4):
        X = moves[i][x]
        Y = moves[i][y]
        new = [coords[x] + X, coords[y] + Y]
        if 0 <= new[x] < bounds[x] and 0 <= new[y] < bounds[y] and maze[new[x], new[y]] == 255:
            gen.append(new)
    return gen

# getting the path
while True:

    gen = moveGen(start, bounds)
    dist = np.inf
    next = []
    # getting the next block
    for i in gen:
        if i not in visited:
            if distance(i, goal) < dist:
                dist = distance(i, goal)
                next = i    
    if next == goal:
        break
    else:
        visited.append(start)
        start = next
        path.append(start)

# completing the maze image
maze = cv2.imread(f"./mazes/{mazeName}.{fileType}")
# defining the goal block color
maze[:, :, 2][goal[x], goal[y]] = 15
maze[:, :, 0][goal[x], goal[y]] = 15
# defining the start block color
maze[:, :, 0][stlessStart[x], stlessStart[y]] = 100
maze[:, :, 1][stlessStart[x], stlessStart[y]] = 15 

for i in path:
    maze[:, :, 2][i[x], i[y]] = 150

cv2.imwrite(f"./mazes/{mazeName}Answer.png", maze)
