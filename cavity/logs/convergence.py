
import numpy as np
import matplotlib.pyplot as plt

ux = np.loadtxt('Ux_0')
uy = np.loadtxt('Uy_0')
p0 = np.loadtxt('p_0')
##data = np.loadtxt(file)

# Put together plot
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

# labels
plt.xlabel('Time (s)')
plt.ylabel('L2 Norm')

plt.tight_layout()
plt.savefig('Case_Convergence.pdf',format='pdf')
# If you "show" before "save", it erases the figure
#plt.show()


