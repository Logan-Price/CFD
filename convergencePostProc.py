import numpy as np
import matplotlib.pyplot as plt

Ux = np.loadtxt('Ux_0')
Uy = np.loadtxt('Uy_0')
p0 = np.loadtxt('p_0')

itr = range(0,len(Ux))
# Put together plot
# valid marker symbols:
#   triangle-shaped: v,<,>,^
#   Cross-like: x,*,+,1,2,3,4
#   Circle-like: o,.,h,p,H,8
#   Blocky & misc: D,d,s,|,_,",",
# Colors: b,g,r,y,c,m,k,w -- blue, green, red, yellow, cyan, magenta, black, white
# Line styles: _,-,--,:
#plt.plot(Ux[:,0],Ux[:,1],'cs') #cyan squares, no line
plt.plot(Uy[:,0],Uy[:,1],'cs',label='Ux') #cyan squares, no line
plt.plot(Ux[:,0],Ux[:,1],'rx',label='Uy') #red x's, no line
plt.plot(p0[:,0],p0[:,1],'k^',label='p0') #black triangles, no line
plt.yscale('log')
plt.legend(loc='upper right')

# labels
plt.xlabel('Time (s)')
plt.ylabel('L2 Norm')



plt.savefig('ConvergencePostProcPlot.pdf',format='pdf')
# If you "show" before "save", it erases the figure
plt.show()



