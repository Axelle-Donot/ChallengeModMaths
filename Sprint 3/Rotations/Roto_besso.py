import numpy as np
import matplotlib.pyplot as plt

racoon = plt.imread("racoon.png","PNG")

racoonbis = racoon.copy() * 0
I = np.arange(768)
J = np.arange(1024)
for bouclei in I :
    for bouclej in J :
        x = bouclej
        ybis = 768-1-bouclei
        mat = np.array([[np.sqrt(3)/2.0,0.5],[-0.5,np.sqrt(3)/2.0]]).dot(np.array([[x],[ybis]]))
        i = (int) (767 - mat[1])
        j = (int) (mat[0])
        if (i>0 and j>0 and i<=767 and j <=1023) :
            racoonbis[bouclei,bouclej] = racoon[i,j]
plt.imshow(racoonbis)
plt.imsave("racoonRotation1.png",racoonbis)