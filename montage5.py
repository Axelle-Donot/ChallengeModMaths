# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

usb = plt.imread('usb.png', 'PNG')
desktop = plt.imread('desktop.png', 'PNG')
desktopTrans = desktop.transpose((1, 0, 2))
print(desktopTrans.shape)
double = np.concatenate((usb, desktopTrans), axis=1)
plt.imshow(double)
