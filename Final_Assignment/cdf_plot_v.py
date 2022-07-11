#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt
import math
x = np.linspace(-25,25,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('log.dat',dtype='double')
#randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def other_cdf(x):
	if(x>0) :
		return 1 - np.exp(x/-2)
	elif(x<0):
		return 0	
		
vec_other_cdf = np.vectorize(other_cdf,otypes=[float])	


plt.plot(x.T,err,'o')#plotting the CDF
plt.plot(x,vec_other_cdf(x),color='red') #plotting the CDF (Continuous Graph Theoretical)
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.legend(["Numerical","Theory"])
plt.show() #opening the plot window
