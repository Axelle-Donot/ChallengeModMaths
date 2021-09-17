# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Création des variables des images
usb = plt.imread('usb.png', 'PNG')
desktop = plt.imread('desktop.png', 'PNG')

# Rotation de l'image desktop.png
desktopTrans = desktop.transpose((1, 0, 2))

print(desktopTrans.shape)

# Ajout des 2 images sur le graphique
double = np.concatenate((usb, desktopTrans), axis=1)

# Affichage des deux images
plt.imshow(double)
