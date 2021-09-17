# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Création des variables des images
usb = plt.imread('usb.png', 'PNG')
usb2 = plt.imread('usb.png', 'PNG')
desktop = plt.imread('desktop.png', 'PNG')

usbcoteacote = np.concatenate((usb, usb2), axis = 1)
print(usbcoteacote.shape)

triple = np.concatenate((usbcoteacote, desktop), axis = 0)
print(triple.shape)

plt.imshow(triple)