import numpy as np
import matplotlib.pyplot as plt

#Axelle
#Challenge des droites
# 24/09/21


#Définition des couleurs

#bleu = np.array([31, 119, 180], dtype = np.uint8)
#orange = np.array([255, 127, 14], dtype = np.uint8)
#vert = np.array ([44,160,44], dtype = np.uint8)


#--------Enveloppe--------

Enveloppe=np.ones ((200,300,3),dtype = np.uint8)*127


#x= np.arange(0,300,1)
#y= np.arange(199,-1,-1)
#X,Y = np.meshgrid(x,y)

#ibleu= Y > -2/3 * X + 200
#iorange= Y < 2/3 * X
#ivert = (Y < -2/3 * X + 200) & (Y < 2/3 * X)

#2/3x
#-2/3x+200 

#Enveloppe[ibleu,:] = bleu
#Enveloppe[iorange,:] = orange
#Enveloppe[ivert,:] = vert

#-------Triangle--------

Triangle=np.ones ((200,300,3),dtype = np.uint8)*127

#x= np.arange(0,300,1)
#y= np.arange(99,-101,-1)
#X,Y = np.meshgrid(x,y)

#iorange=(Y < 100/299 * X) & (Y > -100/299 * X)

#Triangle[iorange,:] = orange



#-------Seychelles-------

jaune = np.array([254,209,65], dtype = np.uint8)
rouge = np.array([210,38,48], dtype = np.uint8)
blanc = np.array([255,255,255], dtype = np.uint8)
vert = np.array([0,122,51], dtype = np.uint8)

Seychelles=np.ones ((501,1001,3),dtype = np.uint8)*(0,47,108)

x= np.arange(0,1001,1)
y= np.arange(500,-1,-1)
X,Y = np.meshgrid(x,y)

ijaune = Y < 3/2 * X
irouge = Y < 3/4 * X
iblanc = Y < 1/3 * X
ivert = Y < 1/6 * X

Seychelles[ijaune,:] = jaune
Seychelles[irouge,:] = rouge
Seychelles[iblanc,:] = blanc
Seychelles[ivert,:] = vert

print ("X :")
print (X)
print ("Y :")
print (Y)


#----Affichage----
plt.imshow(Seychelles)
plt.show()
