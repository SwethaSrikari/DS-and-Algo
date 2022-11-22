import numpy as np

def knapsack_dt(W, V, cap):
    """
    Knapsack dynamic table
    
    :params W: Weights array
    :params V: Values array
    :params cap: Knapsack capacity (weight)
    :params items: number of items
    
    Returns dynamic table
    """
    items = len(W)
    T = np.zeros((items+1, cap+1))
    for i in range(1, items+1):
        for j in range(cap+1):
            if j < W[i-1]:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], T[i-1][j-W[i-1]] + V[i-1])
    return T

def knapsack_items(T, cap, W):
    """
    Items with the maximum value that go into the knapsack
    
    :params T: Calculated Dynamic table
    :params cap: Knapsack capacity (weight)
    :params W: Weights array
    
    Returns indices of items that fit in the knapsack
    """
    items = len(W)
    i, j = items, cap
    print(i, j)
    indices = []
    while j > 0:
        if T[i,j] == T[i-1, j]:
            i, j = i-1, j
        else:
            indices.append(i)
            i, j = i-1, j-W[i-1]
    return indices


# Example 1
W = [3, 1, 3, 4, 2]
V = [2, 2, 4, 5, 3]
cap = 7

T = knapsack_dt(W, V, cap)
print('Dynamic table')
print(T)


print('Items that went into the knapsack are', knapsack_items(T, cap, W))


# Example 2
W = [1, 2, 5, 6, 7]
V = [1, 6, 18, 22, 28]
cap = 11

T = knapsack_dt(W, V, cap)
print('Dynamic table')
print(T)


print('Items that went into the knapsack are', knapsack_items(T, cap, W))