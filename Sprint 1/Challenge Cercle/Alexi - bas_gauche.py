# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 09:38:10 2021

@author: alexi
"""

import numpy as np
import matplotlib.pyplot as plt

gris = np.array([127, 127, 127], dtype = np.uint8)
orange = np.array([255, 127, 14], dtype = np.uint8)

nc, nl = (300, 300)

flag = np.ones((nl, nc, 3), dtype = np.uint8) * 255 

X, Y = np.meshgrid(np.linspace(-nc/3, nc, nc), \
                   np.linspace(nl, -nl/3, nl), \
                   indexing = 'xy')


r = 0.33 * nl

flag[:, :] = gris
flag[(X*X + Y*Y) <= (r*r), :] = orange

plt.imshow(flag)