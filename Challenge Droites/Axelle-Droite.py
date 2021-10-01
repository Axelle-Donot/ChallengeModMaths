import numpy as np
import matplotlib.pyplot as plt

#Axelle
#Challenge des droites
# 24/09/21


#Définition des couleurs

bleu = np.array([31, 119, 180], dtype = np.uint8)
orange = np.array([255, 127, 14], dtype = np.uint8)
Vert = np.array ([44,160,44], dtype = np.uint8)


#--------Enveloppe--------

Enveloppe=np.ones ((200,300,3),dtype = np.uint8)*127


x= np.arange(0,301,1)
y= np.arange(200,-1,-1)
X,Y = np.meshgrid(x,y)

#ibleu= X >= 2/3 * Y

#2/3x
#-2/3x+200 

#Enveloppe[ibleu,:] = bleu
#Enveloppe[iorange,:] = orange
#Enveloppe[ivert,:] = vert

print ("X :")
print (X)
print ("Y :")
print (Y)

#----Affichage----
plt.imshow(Enveloppe)
plt.show()
