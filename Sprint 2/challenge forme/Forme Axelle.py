#challenge forme
#Axelle
#5/10/21

import numpy as np
import matplotlib.pyplot as plt

#----Forme Jaune

x=[-1,-1,-2,-2,-3,-3,-4,-4,-1]
y=[2,3,3,4,4,3,3,2,2]

plt.plot(x, y, "y")

#----Enveloppe

enveloppeX=[-1,-3,-3,-1,-1,-2,-3]
enveloppeY=[0,0,-2,-2,0,-1,0]

plt.plot(enveloppeX,enveloppeY,"b")

#----Maison

maisonX=[4,4,0,2,4,0,0,3,3,2,2,4]
maisonY=[0,4,4,6,4,4,0,0,2,2,0,0]

plt.plot(maisonX,maisonY,"g")

lX=[6,6,5,5,2,2,6]
lY=[-3,-1,-1,-2,-2,-3,-3]

plt.plot(lX,lY,"m")


#----Cadrillage rouge

carre1X=[7,9,9,7,7]
carre1Y=[-3,-3,-1,-1,-3]

carre2X=[8,10,10,8,8]
carre2Y=[-3,-3,-1,-1,-3]

ligneX=[7,10]
ligneY=[-2,-2]

plt.plot(carre1X,carre1Y,"r")
plt.plot(carre2X,carre2Y,"r")
plt.plot(ligneX,ligneY,"r")

#----Cercle

cercleX=np.linspace(-2,2,50)
print (4-cercleX**2)
cercleY=np.sqrt(4-cercleX**2)
plt.plot(cercleX+7,cercleY+2,"k")
plt.plot(cercleX+7,-cercleY+2,"k")

#----Affichage

plt.axis("equal") # Pour que les axes soit proportionnelle
plt.show() 
