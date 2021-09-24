# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 10:04:25 2021

@author: alexi
"""

import numpy as np
import matplotlib.pyplot as plt 

bleu = np.array([0, 0, 255], dtype = np.uint8)
vert = np.array([22, 184, 78], dtype = np.uint8)
orange = np.array([255, 127, 14], dtype = np.uint8)

nc, nl = (400, 300)

flag = np.ones((nl, nc, 3), dtype = np.uint8) * 255 

X, Y = np.meshgrid(np.linspace(-nc/2 + 0.5, nc/2 - 0.5, nc), \
                   np.linspace(nl/2 - 0.5, -nl/2 + 0.5, nl), \
                    indexing = 'xy')
                            
r = 0.4 * nl
r2 = 0.35 * nl

flag[:,:] = bleu
flag[(X*X + Y*Y) <= (r*r), :] = vert
flag[(X*X + Y*Y) <= (r2*r2), :] = bleu

plt.imshow(flag)