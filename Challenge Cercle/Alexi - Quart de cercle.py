# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 09:25:02 2021

@author: alexi
"""

import numpy as np
import matplotlib.pyplot as plt

orange = np.array([255, 127, 14], dtype = np.uint8)
bleu = np.array([50, 50, 135], dtype = np.uint8)

# On définit la taille de l'image 
nc, nl= (300, 300)

flag = np.ones((nl, nc, 3), dtype = np.uint8) * 255 

# nl = Hauteur, nc = Largeur

X, Y = np.meshgrid(np.linspace(0, nc/2 -  0.5, nc),\
                   np.linspace(nl/2 - 0.5, 0, nl), \
                   indexing = 'xy')

    
# Rayon cercle : 50% de la hauteur
r = 0.5 * nl
flag[:, :] = bleu
flag[ (X*X + Y*Y) <= (r*r) , :] = orange
plt.imshow(flag)