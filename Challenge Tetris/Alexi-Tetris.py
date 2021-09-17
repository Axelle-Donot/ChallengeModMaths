# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

gris = np.array([127, 127, 127], dtype = np.uint8)
bleu = np.array([31, 119, 180], dtype = np.uint8)
orange = np.array([255, 127, 14], dtype = np.uint8)
vert = np.array([44, 160, 44], dtype = np.uint8)

l, h = (300, 200)

fondgris = 300 * np.ones((h, l, 3), dtype = np.uint8)
fondgris[0:300,0:300,:] = gris
fondgris[0:300, 0:50,:] = bleu
fondgris[0:150, 50:100,:] = orange
fondgris[50:100, 100:150,:] = orange
fondgris[150:200, 150:250,:] = vert
fondgris[100:150, 200:300,:] = vert

plt.imshow(fondgris)
plt.show()