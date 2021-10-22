# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 10:04:25 2021

@author: alexi
"""

import numpy as np
import matplotlib.pyplot as plt 

bleu = np.array([0, 0, 200], dtype = np.uint8)
vert = np.array([22, 184, 78], dtype = np.uint8)
orange = np.array([255, 127, 14], dtype = np.uint8)

nc, nl = (500, 300)

flag = np.ones((nl, nc, 3), dtype = np.uint8) * 255 

X, Y = np.meshgrid(np.linspace(-nc/2, nc/2, nc), \
                   np.linspace(nl/2, -nl/2, nl), \
                    indexing = 'xy')
                            
r = 0.35 * nl
r2 = 0.3 * nl

# Partie demi cercles
#flag[0:150,:] = bleu
ivertBas = (X*(X+150) + Y*Y <= (r*r)) & (X*(X+150) + Y*Y > (r2*r2)) & (Y <= 0)
iorangeHaut = (X*(X-150) + Y*Y <= (r*r)) & (X*(X-150) + Y*Y > (r2*r2)) & (Y > 0)
ivertHaut = (X*(X+150) + Y*Y <= (r*r)) & (X*(X+150) + Y*Y > (r2*r2)) & (Y > 0)
iorangeBas = (X*(X-150) + Y*Y <= (r*r)) & (X*(X-150) + Y*Y > (r2*r2)) & (Y <= 0)

# Partie affectations dans le bon ordre
flag[:,:] = bleu
flag[iorangeHaut] = orange
flag[ivertHaut] = vert
flag[ivertBas] = vert
flag[iorangeBas] = orange

plt.imshow(flag)