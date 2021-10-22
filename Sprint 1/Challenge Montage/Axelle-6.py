import numpy as np
import matplotlib.pyplot as plt

imgUsb = plt.imread("usb.png", "PNG")
imgordi = plt.imread("desktop.png", "PNG")


#--------------1----------------

imgfinal = np.concatenate ((imgUsb,imgordi), axis=1)

#--------------2----------------

#imginter = np.concatenate ((imgUsb,imgUsb),axis=1)
#imgfinal = np.concatenate ((imginter,imgordi),axis=0)

#--------------3----------------

#imgfinal = np.concatenate ((imgUsb,imgUsb[:,::-1]), axis=1)

#--------------4----------------

#imgfinal = np.concatenate ((imgUsb,imgUsb[::-1]), axis=1)

#--------------5----------------

imgordi1 = imgordi.transpose(1,0,2)

imgfinal = np.concatenate ((imgUsb,imgordi1) , axis=1)


#--------------6----------------

#imgUsb1 = imgUsb.transpose (1,0,2)
#imgordi1 = imgordi.transpose (1,0,2)

#imgfinal = np.concatenate ((imgUsb1,imgordi1[:,::-1]), axis=0)


#---------Affichage-------------

plt.imshow(imgfinal)
plt.show()
