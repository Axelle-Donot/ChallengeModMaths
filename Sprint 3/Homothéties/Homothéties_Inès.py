"Homothétie de centre A(512,384) et de rapport 1/sqrt(2)"
import numpy as np
import matplotlib.pyplot as plt

racoon = plt.imread('racoon.png','PNG')

racoonbis = racoon.copy() * 0
I = np.arange(768)
J = np.arange(1024)
for ibiscus in I:
    for jbiscus in J:
        xbiscus = jbiscus
        ybiscus = 768 - 1 - ibiscus
        mat = np.array([[2.0/np.sqrt(2),0], [0, 2.0/np.sqrt(2)]]).dot(np.array([[xbiscus],[ybiscus]])) - np.array([[212],[158]]) 
        i = int(767 - mat[1]) 
        j = int(mat[0])
        if (i > 0 and j > 0 and i <= 767 and j<= 1023):
            racoonbis[ibiscus,jbiscus] = racoon[i,j]
                           
plt.imshow(racoonbis)
plt.imsave("racoonHomothetie.png", racoonbis)