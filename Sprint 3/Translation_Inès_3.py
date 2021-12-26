import numpy as np
import matplotlib.pyplot as plt

racoon = plt.imread("racoon.png","PNG")

""" Translation du vecteur u(-300,-150)"""


racoonbis = racoon.copy() * 0

I = np.arange(768)
J = np.arange(1024)

for ibis in I :
    for jbis in J :
        xbis = jbis
        ybis = 768 - 1 - ibis
        mat = np.array([[1,0],[0,1]]).dot(np.array([[xbis],[ybis]])) - np.array([[-300],[-150]])
        i = 767 - mat[1]
        j = mat[0]
        if (i > 0 and j > 0 and i <= 767 and j <= 1023):
            racoonbis[ibis,jbis] = racoon[i,j]
            
plt.imshow(racoonbis)
plt.imsave("racoonTranslation_3.png",racoonbis)      