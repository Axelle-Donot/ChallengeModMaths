# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 09:55:34 2021

@author: alexi
"""

import numpy as np
import matplotlib.pyplot as plt

bleu = np.array([50, 50, 135], dtype = np.uint8)
orange = np.array([255, 127, 14], dtype = np.uint8)

nc, nl = (300, 300)

flag = np.ones((nl, nc, 3), dtype = np.uint8) * 255

X, Y = np.meshgrid(np.linspace(-nc/2 + 0.5, nc/2 - 0.5, nc), \
                   np.linspace(nl/2 - 0.5, -nl/2 + 0.5, nl), \
                               indexing = 'xy')

r = 0.5 * nl
r2 = 0.25 * nl

flag[:,:] = bleu
flag[(X*X + Y*Y) <= (r*r), :] = orange
flag[(X*X + Y*Y) <= (r2*r2), :] = bleu

plt.imshow(flag)