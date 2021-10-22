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

A=np.ones ((201,301,3),dtype = np.uint8)* (31,119,180)

x=np.arange(-100,201,1)
y=np.arange(100,-101,-1)
X,Y = np.meshgrid(x,y)

r1=80;
r2=70;

ivert = (X*X + Y*Y) <= r1*r1
ibleu = (X*X + Y*Y) <= r2*r2

A[ivert,:]=vert
A[ibleu,:]=bleu

x1=np.arange(-200,101,1)
y1=np.arange(100,-101,-1)
X1,Y1 = np.meshgrid(x1,y1)

iorange = (X1*X1 + Y1*Y1) <= r1*r1
ibleu2 = (X1*X1 + Y1*Y1) <= r2*r2

A[iorange,:]=orange
A[ibleu2,:]=bleu

print ("X :")
print (X)
print ("Y :")
print (Y)



#---Affichage---

plt.imshow(A)
plt.show()
