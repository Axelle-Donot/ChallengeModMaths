import numpy as np
import matplotlib.pyplot as plt

# Tetrise 17/09/21

tetris = 255 * np.ones((200, 300,3), dtype = np.uint8)

tetris [::]= (127, 127, 127)
tetris [:,0:51] = (31, 119, 180)
tetris [0:151,50:101] = (255, 127, 14)
tetris [50:101,100:151] = (255, 127, 14)
tetris [150:201,150:251] = (44,160,44)
tetris [100:151,200:301] = (44,160,44)

plt.imshow(tetris)
plt.show()
