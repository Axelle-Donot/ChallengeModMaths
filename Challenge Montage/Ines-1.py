import matplotlib.pyplot as plt
import numpy as np

                         #COTE A COTE
usb = plt.imread('usb.png','PNG')
desktop = plt.imread('desktop.png','PNG')

usbtab = 255 * np.ones((600, 300,3), dtype = np.uint8) #on crée un tableau blanc qui va contenir notre image
usbtab = usb #on met l'image dans le tableau

desktoptab = 255 * np.ones((600, 600,3), dtype = np.uint8)
desktoptab = desktop

final = np.concatenate((usbtab,desktoptab), axis =1) #on concatene les tableaux
plt.imshow(final) #on affiche le tout
plt.show()

