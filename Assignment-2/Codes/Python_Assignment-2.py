import numpy as np
from numpy import random as RN 


N = 6

pr_1 = 1/3
pr_2 = 1/6

print("Theoretical Probability : ",(1-pr_1-pr_2+pr_1*pr_2))


# Let x take any value from 1 to 6 inclusive over the size N ,
x = RN.randint(1, 7, size=N)
# and if x = {1,2} , then we shall take that A has won the race
# and if x = {3} , then we shall take that B has won the race
# and for other values of x we shall take that neither has won the match

x_1 = np.count_nonzero(x==1) + np.count_nonzero(x==2)
x_2 = np.count_nonzero(x==3)

print("Practical Probability : ",1 - x_1/N - x_2/N + (x_1/N)*(x_2/N))
