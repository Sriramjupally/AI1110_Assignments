#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import scipy 
import matplotlib.pyplot as plt



maxrange=60
maxlim=2.5
x = np.linspace(-maxlim,maxlim,maxrange) #points on the x axis for practical
x1 = np.linspace(-maxlim,maxlim,maxrange*2) #points on the x axis for theoretical
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list


randvar = np.loadtxt('tri.dat',dtype='double') # Data


for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

plt.plot(x[0:(maxrange-1)].T,pdf,'o')


def func(x):
	if (x<0):
		return 0
	elif (x>=0 and x<1):
		return x
	elif (x>=1 and x<=2):
		return 2-x
	else:
		return 0



vec_other_cdf = np.vectorize(func,otypes=[float])	

plt.plot(x,vec_other_cdf(x),color='red')#plotting the CDF
# plt.legend(["Numerical", "Theory"])

# #plt.plot(x,func1(x),color='blue',linestyle='dashed')#plotting the CDF

# for i in range(60):
# 	y.append(func(x[i]))

# plt.plot(x,y,color='red')#plotting the CDF


plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.show()
