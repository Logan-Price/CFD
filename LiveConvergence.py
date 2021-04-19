#####################################################################################
###                          Live plotting of Residuals                           ###
#####################################################################################

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation  import FuncAnimation

def animate(i):
    data = pd.read_csv('postProcessing/residuals/0/residuals_0.dat', sep='\t', skiprows=1)
    data.dropna(inplace=True)
    data.columns = data.colunms.str.strip('# ')
    itr = data['Time']
    Ux = data['Ux']
    Uy = data['Uy']
    p0 = data['p']
    plt.cla()
    plt.plot(itr,Ux,'cs',label='Ux')
    plt.plot(itr,Uy,'rs',label='Uy')
    plt.plot(itr,p0,'ks',label='p0')
    plt.yscale('log')
    plt.legend(loc='upper right')
    plt.xlabel('Itteration')
    plt.ylabel('L2 Norm')
    
ani = FuncAnimation(plt.gcf(),animate, interval=1000)
plt.tight_layout()
plt.show()
