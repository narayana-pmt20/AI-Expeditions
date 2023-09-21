from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# 1D array
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

# 2D array
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3,4))
print(x)


sns.distplot(random.normal(size=1000), hist=False)
plt.show()