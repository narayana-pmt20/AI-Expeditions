import numpy as np

arr = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])

print("Printing from 5th index :: ", arr[5:])

print("Printing till 5th index :: (does not include 5th index)", arr[:5])

print("Printing from 5th to 14th :: ", arr[5:14])

print("Printing from 5th to 14th, skip every second number :: ", arr[5:14:2])

print("\n\n\n\n")

arr2 = np.array([
                [1,2,3,4,5,6,7,8,9,0], 
                [11,12,13,14,15,16,17,18,19,20],
                [21,22,23,24,25,26,27,28,29,30],
                [31,32,33,34,35,36,37,38,39,40],
                [41,42,43,44,45,46,47,48,49,50],
                [51,52,53,54,55,56,57,58,59,60],
                [61,62,63,64,65,66,67,68,69,70],
                [71,72,73,74,75,76,77,78,79,80],
                [81,82,83,84,85,86,87,88,89,90],
                [91,92,93,94,95,96,97,98,99,100]
                ])
print("Printing array 2 :: \n", arr2)

print("Printing from first row ::", arr2[0][2:6])

print("\n\n", "-----------------------------------------",
      "\nPrinting first three elements from all elements ::", arr2[0:3, 0:3])

print("\n\n", "-----------------------------------------",
      "\nPrinting third and fourth elements in all the rows ::", arr2[:, 2:4])


print("\n\n", "-----------------------------------------",
      "\nPrint only first element from all the records ::", arr2[:, 0])

print("\n\n", "-----------------------------------------",
      "\nPrint only first element from all the records as an NP array ::", np.array(arr2[:, 0]))


