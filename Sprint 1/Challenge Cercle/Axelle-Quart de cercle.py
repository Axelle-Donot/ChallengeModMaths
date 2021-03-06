import numpy as np
import matplotlib.pyplot as plt

#axelle
#challenge des cercles
#1/10/21


#definition des couleurs
bleu = np.array([31, 119, 180], dtype = np.uint8)
orange = np.array([255, 127, 14], dtype = np.uint8)
vert = np.array ([44,160,44], dtype = np.uint8)

# --quart de cercle dans un carré 

A=np.ones ((201,201,3),dtype = np.uint8)*(31,119,180)

x=np.arange(0,201,1)
y=np.arange(200,-1,-1)
X,Y = np.meshgrid(x,y)

r=200

iorange = (X*X+Y*Y) <= r*r
A[iorange,:]=orange


print ("X :")
print (X)
print ("Y :")
print (Y)



#---Affichage---

plt.imshow(A)
plt.show()
