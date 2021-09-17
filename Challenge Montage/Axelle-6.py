import numpy as np
import matplotlib.pyplot as plt

imgUsb = plt.imread("usb.png", "PNG")
imgordi = plt.imread("desktop.png", "PNG")

imgUsb1 = imgUsb.transpose (1,0,2)
imgordi1 = imgordi.transpose (1,0,2)

imgfinal = np.concatenate ((imgUsb1,imgordi1[:,::-1]), axis=0)

plt.imshow(imgfinal)
plt.show()
