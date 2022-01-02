import numpy as np
import matplotlib.pyplot as plt

racoon = plt.imread("racoon.png","PNG")

racoonbis= racoon.copy() * 0
I=np.arange(768)
J=np.arange(1024)
for ibiscus in I:
    for jbiscus in J:
        xbis=jbiscus
        ybis=768-1-ibiscus
        mat=np.array([[0,1],[1,0]]).dot(np.array([[xbis],[ybis]]))
        i= (int) (767 - mat[1])
        j= (int) (mat[0])
        if (i>0 and j>0 and i<=767 and j<=1023) :
            racoonbis[ibiscus,jbiscus]=racoon[i,j];
                
plt.imshow(racoonbis);
plt.imsave("racoonSymetrie1.png",racoonbis);