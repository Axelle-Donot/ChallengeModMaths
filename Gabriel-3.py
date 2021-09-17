# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

usb = plt.imread("usb.png", "PNG")

miror = usb[:,::-1] #[:,::-1]

usbAll = np.concatenate((usb,miror),axis=1)
print(usbAll.shape)
plt.imshow(usbAll)
