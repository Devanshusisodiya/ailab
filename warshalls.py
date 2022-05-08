import numpy as np

inf = np.inf
n = 4 # NODES

Q = np.array([
    [7,5,inf,inf],
    [7,inf,inf,2],
    [inf,3,inf,inf],
    [4,inf,1,inf]
])

for k in range(n):
    for i in range(n):
        for j in range(n):
            Q[i, j] = min(Q[i, j], Q[i, k] + Q[k, j])
    print(k+1)
    print(Q)

print("final answer")
print(Q)