import numpy as np
import matplotlib.pyplot as plt

raton = plt.imread('racoon.png','PNG')

ratontab = 255 * np.ones((610,813,3), dtype = np.uint8) #on crée un tableau blanc qui va contenir notre image
ratontab = raton #on met l'image dans le tableau
plt.imshow(ratontab);

plt.show();