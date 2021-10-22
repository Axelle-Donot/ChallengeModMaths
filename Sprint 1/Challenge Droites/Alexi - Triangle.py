# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 17:56:23 2021

@author: alexi
"""

import numpy as np
import matplotlib.pyplot as plt

# On définit les couleurs avant tout
gris = np.array([127, 127, 127], dtype = np.uint8)
orange = np.array([255, 127, 14], dtype = np.uint8)

# On définit la taille de l'image 
nc, nl= (300, 200)

# On initialise l'image blanche avec les coordonnées rentrées
flag = np.ones((nl, nc, 3), dtype = np.uint8) * 255

# On crée les coordonnées avec une origine au centre de l'image
X, Y = np.meshgrid(np.linspace(-nc/2 + 0.5, nc/2 -  0.5, nc),\
                   np.linspace(nl/2 - 0.5, -nl/2 + 0.5, nl), \
                   indexing = 'xy')

# iorange a son ordonnée comprise entre -(1/3)x - 52 <= y <= (1/3)x + 50
iorange = (Y >= - (1 / 3) * X - 52) & (Y <= (1 / 3) * X + 50)

# igris1 a son ordonnée Y <= -(1/3)x - 52
igris1 = (Y <= - (1 / 3) * X - 52)

# igris2 a son ordonnée Y >= (1/3)x + 50
igris2 = (Y >= (1 / 3) * X + 50)

# On affecte les couleurs à chaque variables
flag[iorange,:] = orange
flag[igris1,:] = gris
flag[igris2,:] = gris

# On affiche le fameux triangle
plt.imshow(flag)