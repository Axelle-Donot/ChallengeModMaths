import matplotlib.pyplot as plt
import numpy as np

"""                          COTE A COTE
usb = plt.imread('usb.png','PNG')
desktop = plt.imread('desktop.png','PNG')

usbtab = 255 * np.ones((600, 300,3), dtype = np.uint8) #on crée un tableau blanc qui va contenir notre image
usbtab = usb #on met l'image dans le tableau

desktoptab = 255 * np.ones((600, 600,3), dtype = np.uint8)
desktoptab = desktop

final = np.concatenate((usbtab,desktoptab), axis =1) #on concatene les tableaux
plt.imshow(final) #on affiche le tout
plt.show()
"""


"""                   COTE A COTE ET AU DESSUS
usb1 = plt.imread('usb.png','PNG')
usb2 = usb1

desktop = plt.imread('desktop.png','PNG')

desktoptab = 255 * np.ones((600, 600,3), dtype = np.uint8)
desktoptab = desktop
usbtab1 = 255 * np.ones((600, 300,3), dtype = np.uint8)

usbtab2 = usbtab1 #création plus rapide, clonage de tableau

usbtab1 = usb1
usbtab2 = usb2

usbcolle = np.concatenate((usbtab1,usbtab2), axis =1)

final = np.concatenate((usbcolle,desktoptab), axis =0)
plt.imshow(final)
plt.show
"""



