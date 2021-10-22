# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 18:11:47 2021

@author: alexi
"""

import numpy as np
import matplotlib.pyplot as plt

# On définit les couleurs avant tout
bleu = np.array([0, 0, 135], dtype = np.uint8)
rouge = np.array([255, 0, 0], dtype = np.uint8)
vert = np.array([5, 119, 0], dtype = np.uint8)
jaune = np.array([255, 216, 0], dtype = np.uint8)

# On définit la taille de l'image 
nc, nl= (1000, 500)

# On initialise l'image blanche avec les coordonnées rentrées
flag = np.ones((nl, nc, 3), dtype = np.uint8) * 255

# On crée les coordonnées avec une origine au centre de l'image
X, Y = np.meshgrid(np.linspace(0, nc, nc),\
                   np.linspace(-nl, 0, nl), \
                   indexing = 'xy')
    
ibleu = (Y <= (3/2) * X) & (Y <= - (3/2) * X)
ijaune = (Y <= 1) & (Y >= - (3/2) * X) & (Y <= - (3/4) * X)
irouge = (Y >= - (3/4) * X) & (Y <= - (1 / 3) * X)
ivert = (Y >= - (1 / 6) * X)

flag[ibleu,:] = bleu
flag[ijaune,:] = jaune
flag[irouge,:] = rouge
flag[ivert,:] = vert

plt.imshow(flag)
