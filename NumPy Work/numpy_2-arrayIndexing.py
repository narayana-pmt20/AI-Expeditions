import numpy as np

arr = np.array([1,2,3,4,5,6])

print(arr[0])
print(arr[1])


print(arr[1] + arr[3])


#accessing 2D array
arr2 = np.array([[1,2,3,4,5], [6,7,8,9,0]])
print(arr2)
print(arr2[0][3])


#accessing 3D array
arr3 = np.array([[[1,2, 19],[3,4, 20],[5,6, 21]],[[7,8,22],[9,10,23],[11,12,24]], [[13,14,25],[15,16,26],[17,18,27]]])
print(arr3)
print(arr3[1][2][2])
print(arr3[-1][-1][-1])