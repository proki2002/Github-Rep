import numpy as np 
from matplotlib import pyplot as plt 
import pandas as pd 
from numpy import nan


class W:
    def __init__(self,pomiary:list,l:int):
        self.p=np.array(pomiary)
        self.l=l
    def wykres(self):
        self.suma=[np.sum(self.p[:x]) for x in range(len(self.p))]
        self.p=self.p*10**5/self.l
        plt.plot(self.suma,self.p)
        plt.show()

f = pd.read_excel('F:\Github Rep\Lab Fizyka 1\dane.xlsx')
c=f[f.columns[0]].values.tolist()
z=f[f.columns[1]].values.tolist()
z=[x for x in z if str(x)!='nan'] #20 przejść o 1/2 lambda ergo zmiana o 10 lambda
c=[x for x in c if str(x)!='nan']
lc=636
lz=532


z=W(z,lz)
z.wykres(), z.p, z.suma

c=W(c,lc)
c.wykres(), c.p, c.suma