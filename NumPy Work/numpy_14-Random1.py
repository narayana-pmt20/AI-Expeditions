from numpy import random
x = random.randint(100000, size=2)
print(x)

#gives an array of random numbers
x = random.randint(100000, size=(3,5))
print(x)

# 2D array, with floats
x = random.rand(3,5)
print(x)


x = random.choice([3, 5, 7, 9])
print(x)

# creating an array of defined dimension from the list of numbers given
x = random.choice([3, 5, 7], size=(3, 5))
print(x)