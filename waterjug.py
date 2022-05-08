# THIS IS THE SCRIPT FOR SOLVING THE
# WARTER JUG PROBLEM USING BFS SEARCH 

# initialising data
init = [0, 0]
goal = [2, 0]

def moveGen(node):
    '''
        This routine creates neighbours of the input
        node on the basis of the production rules
        which are already decided by the definition of the
        water jug problem
    '''
    children = []
    if node[0] < 4:
        children.append([4, node[1]])
    if node[1] < 3:
        children.append([node[0], 3])
    if node[0] > 0:
        children.append([0, node[1]])
    if node[1] > 0:
        children.append([node[0], 0])
    if (node[0] + node[1]) >= 4 and node[1] > 0:
        children.append([4, node[1]-(4-node[0])])
    if (node[0] + node[1]) >= 3 and node[0] > 0:
        children.append([node[0]-(3-node[1]), 3])
    if (node[0] + node[1]) <= 4 and node[1] > 0:
        children.append([node[0] + node[1], 0])
    if (node[0] + node[1]) <= 3 and node[0] > 0:
        children.append([0, node[0] + node[1]])
    if node == [0, 2]:
        children.append([0, 2])

    return children

def getUniqueChildren(children):
    '''
        This routine returns children that arent in the visited list
        or simply havent been visited
    '''
    unique = []
    for child in children:
        if child not in visited:
            unique.append(child)
    return unique

def enQueue(a, b):
    '''
        This routine enqueues the elements of vector a in 
        vector b
    '''
    for i in a:
        b.insert(0, i)
    return b

# initialising the open and visited lists
open = []
visited = []

currentNode = init

while currentNode:
    if currentNode == goal:
        # add this node to the visited list
        visited.append(currentNode)
        break
    elif currentNode in visited:
        # if by some chance we get a child that is already visited
        # we simply drop this node and choose the next from the open
        currentNode = open.pop()
    else:
        # adding the node to the
        # visited list
        visited.append(currentNode)
        # generating children
        children = moveGen(currentNode)
        if children != []:
            # get children which arent already visited
            children = getUniqueChildren(children)
            open = enQueue(children, open)
        # get the current node from the front of the queue
        currentNode = open.pop()

print(visited)