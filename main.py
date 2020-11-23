import matplotlib.pyplot as plt
import numpy as np

def hypergeometric_random_variable( M, R, N ) : 
  # Your code goes here 
  
  
  
# You shouldn't need to modify anything from here onwards this just plots your variable
xvals, yvals = np.zeros(100), np.zeros(100) 
for i in range(100) : xvals[i], yvals[i] = i+1, hypergeometric_random_variable(4,4,12)

plt.plot( xvals, yvals, 'ko' )
plt.savefig("choice_var.png")
