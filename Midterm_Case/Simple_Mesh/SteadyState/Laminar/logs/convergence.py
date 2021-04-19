#####################################################################################
###                 Residuals Plots to Ilustrate Convergence                      ###
#####################################################################################
'''
Residuals are the differences in the value of a quantity (for example x-velocity or y velocity or p,ecc.) between two iterations.

Residuals can be found by the equation:       ( for Matrix System: Ax = b)
    --> L2 Norm (residual) = 1/n * SUMATION[ Abs( b - Ax) ]
    - OpenFoam's built-in utilities calculate the values ploted here. The equation is just for reference

'''
import numpy as np
import matplotlib.pyplot as plt

# Residuals to be ploted
ux = np.loadtxt('Ux_0')
uy = np.loadtxt('Uy_0')
p0 = np.loadtxt('p_0')

# Put together plot/ Customization
# valid marker symbols:
#   triangle-shaped: v,<,>,^
#   Cross-like: x,*,+,1,2,3,4
#   Circle-like: o,.,h,p,H,8
#   Blocky & misc: D,d,s,|,_,",",
# Colors: b,g,r,y,c,m,k,w -- blue, green, red, yellow, cyan, magenta, black, white
# Line styles: _,-,--,:

plt.plot(ux[:,0],ux[:,1],'bs', label = 'U_x') #blue squares, no line
plt.plot(uy[:,0],uy[:,1],'rx', label = 'U_y') #red x's, no line
plt.plot(p0[:,0],p0[:,1],'ko', label = 'p_0') #black circles, no line
plt.yscale('log')
plt.legend()

# Axis labels
plt.xlabel('Iteration', fontsize=13)
plt.ylabel('L2 Norm (Residual value)', fontsize=13)

plt.tight_layout()
plt.savefig('Case_Convergence.jpg')
#plt.show()    ## If you "show" before "save", it erases the figure
