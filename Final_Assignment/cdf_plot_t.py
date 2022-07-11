#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if



x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
randvar = np.loadtxt('tri.dat', dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
plt.plot(x.T,err,marker='o')#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

def func(x):
	if(x <= 0 ):
		return 0
	if(x>0 and x<1):
		return x*x/2
	if(x>=1 and x<2):
		return (1 - ((2-x)**2)/2)
	if(x>=2):
		return 1


		
# for i in range(30):
# 	y.append(func(x[i]))
vec_other_cdf = np.vectorize(func,otypes=[float])	

plt.plot(x,vec_other_cdf(x),color='red')#plotting the CDF
plt.legend(["Numerical", "Theory"])


#if using termux
#plt.savefig('../figs/uni_cdf.pdf')
#plt.savefig('../figs/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
