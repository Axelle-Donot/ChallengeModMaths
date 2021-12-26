"Homothétie de centre A(512,384) et de sqrt(2)"
import numpy as np
import matplotlib.pyplot as plt

racoon = plt.imread('racoon.png','PNG')

racoonbis = racoon.copy() * 0
I = np.arange(768)
J = np.arange(1024)
for ibis in I:
    for jbis in J:
        xbis = jbis
        ybis = 768 - 1 - ibis
        mat = np.array([[np.sqrt(2)/2,0], [0,np.sqrt(2)/2]]).dot(np.array([[xbis],[ybis]])) - np.array([[212],[158]]) 
        i = int(767 - mat[1]) 
        j = int(mat[0])
        if (i > 0 and j > 0 and i <= 767 and j<= 1023):
            racoonbis[ibis,jbis] = racoon[i,j]
                           
plt.imshow(racoonbis)
plt.imsave("racoonnHomothetie.png", racoonbis)