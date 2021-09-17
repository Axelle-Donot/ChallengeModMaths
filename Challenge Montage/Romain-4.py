# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
import matplotlib.pyplot as plt

usb = 255 * np.ones((200, 100,3), dtype = np.uint8)
usbImg = plt.imread('usb.png', 'PNG')
usb=usbImg

usbBis = 255 * np.ones((200, 100,3), dtype = np.uint8)
usbImgBis = plt.imread('usb.png', 'PNG')
usbTourne = usbImgBis[::-1]
usbBis=usbTourne


final = np.concatenate((usb, usbBis), axis=1)
plt.imshow(final)
plt.show