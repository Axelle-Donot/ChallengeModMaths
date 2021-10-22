# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 09:44:01 2021

@author: alexi
"""

import numpy as np
import matplotlib.pyplot as plt

# On définit les couleurs avant tout
gris = np.array([127, 127, 127], dtype = np.uint8)
bleu = np.array([31, 119, 180], dtype = np.uint8)
orange = np.array([255, 127, 14], dtype = np.uint8)
vert = np.array([44, 160, 44], dtype = np.uint8)

# On définit la taille de l'image 
nc, nl= (300, 200)

# On initialise l'image blanche avec les coordonnées rentrées
flag = np.ones((nl, nc, 3), dtype = np.uint8) * 255

# On crée les coordonnées avec une origine au centre de l'image
X, Y = np.meshgrid(np.linspace(-nc/2 + 0.5, nc/2 -  0.5, nc),\
                   np.linspace(nl/2 - 0.5, -nl/2 + 0.5, nl), \
                   indexing = 'xy')
# booléen pour chaque fonction :
# igris a son ordonnée comprise entre : (2/3)x <= y <= -(2/3)x
igris = (Y <= -2 * X / 3) & (Y >= 2 * X / 3)

# iorange a son ordonnée comprise entre : -(2/3)x <= y <= (2/3)x
iorange = (Y >= -2 * X / 3) & (Y <= 2 * X / 3)

# ibleu a son ordonnée comprise entre : -(2/3)x <= y <= (2/3)x et supérieure ou égale à 0
ibleu = (Y >= 0) & (Y >= -2 * X /3) & (Y >= 2 * X / 3)

# igris a son ordonnée comprise entre (2/3)x <= y <= -(2/3)x et inférieure ou égale à 0
ivert = (Y <= 0) & (Y <= -2 * X / 3) & (Y <= 2 * X / 3)

# On affecte les couleurs à chaque variables
flag[igris,:] = gris
flag[iorange,:] = orange
flag[ibleu,:] = bleu
flag[ivert,:] = vert

# On affiche la belle et magnifique enveloppe
plt.imshow(flag)
