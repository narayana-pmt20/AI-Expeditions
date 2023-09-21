import numpy as np


#creating Arrays
arr = np.array((1, 2, 3, 4, 5))
print(arr)

# zero dim array
arr = np.array(42)
print(arr)
print(np.ndim(arr))


# 1- dim array
arr = np.array( [ 1, 2, 3 ])
print(arr)
print(np.ndim(arr))

# 2- dim array
arr = np.array( [ [1,2], [3,4], [5,6] ])
print(arr)
print(np.ndim(arr))

# 3- dim array
arr = np.array( [ [[1,2],[3,4]], [[5,6],[7,8]], [[9,10],[11,12]] ])
print(arr)
print(np.ndim(arr))

# 4- dim array
arr = np.array( [ [[[1,2],[3,4]],[[5,6],[7,8]]], [[[9,10],[11,12]],[[13,14],[14,15]]], [[[16,17],[18,19]],[[20,21],[22,23]]] ])
print(arr)
print(np.ndim(arr))
