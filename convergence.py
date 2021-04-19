#####################################################################################
###                 Residuals Plots to Illustrate Convergence                     ###
#####################################################################################
'''
Residuals are the differences in the value of a quantity (for example x-velocity, y-velocity or p, ecc.) between two iterations.

Residuals can be found by the equation:       ( for Matrix System: Ax = b)
    --> L2 Norm (residual) = 1/n * SUMATION[ Abs( b - Ax) ]
    - OpenFoam's built-in utilities calculate the values ploted here. The equation is just for reference
    
If Turbulence Models are being used in the simulaton, the turbulance values will be plotted also (k, epsilon, nuTilda)
'''
import numpy as np
import matplotlib.pyplot as plt
import os as os

# Residuals to be ploted always
ux = np.loadtxt('Ux_0')
uy = np.loadtxt('Uy_0')
uz = np.loadtxt('Uz_0')
p0 = np.loadtxt('p_0')

# If Turbulenc Model Present
kbool = False
ebool = False
nuTildabool = False
if os.path.isfile("k_0") == True:  # Ensure the variable is being used
    k = np.loadtxt('k_0')
    kbool = True
if os.path.isfile("epsilon_0") == True:
    epsilon = np.loadtxt('epsilon_0')
    ebool = True
if os.path.isfile("nuTilda_0") == True:
    nuTilda = np.loadtxt('nuTilda_0')
    nuTildabool = True

# Put together plot/ Customization
# valid marker symbols:
#   triangle-shaped: v,<,>,^
#   Cross-like: x,*,+,1,2,3,4
#   Circle-like: o,.,h,p,H,8
#   Blocky & misc: D,d,s,|,_,",",
# Colors: b,g,r,y,c,m,k,w -- blue, green, red, yellow, cyan, magenta, black, white
# Line styles: _,-,--,:

os.chdir("..")
plt.plot(ux[:,0],ux[:,1],'bs', label = 'U_x') #blue squares, no line
plt.plot(uy[:,0],uy[:,1],'rx', label = 'U_y') #red x's, no line
plt.plot(uz[:,0],uz[:,1],'g.', label = 'U_z') #blue squares, no line
plt.plot(p0[:,0],p0[:,1],'ko', label = 'p') #black circles, no line
# Turbulence
if kbool == True:
    plt.plot(k[:,0],k[:,1],'y+', label = 'k') 
if ebool == True:
    plt.plot(epsilon[:,0],epsilon[:,1],'cv', label = 'epsilon')
if nuTildabool == True:
    plt.plot(nuTilda[:,0],nuTilda[:,1],'y+', label = 'nuTilda')


# Axis labels
#plt.xlabel('Time (s)', fontsize=14)  # TIme Accurate Solvers
plt.xlabel('Iteration', fontsize=14)  # Steady - State Solvers
plt.ylabel('L2 Norm (Residual value)', fontsize=14)
plt.yscale('log')
plt.legend()
plt.tight_layout()
plt.savefig('Case_Convergence.png')
#plt.show()    ## If you "show" before "save", it erases the figure 