# -*- coding: utf-8 -*-
"""
Optical fits image processing for M86

"""

#load packages and give them names
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

#read in a .fits file 
#FITS is popular file format used for images in astronomy
data = fits.open('M86.fits')

#.info indicates how many objects are in the list
# there is only one object called PRIMARY
data.info()
#view header information
print(data[0].header)

#make an ordinary 2D array from the image data
#and display using the function imshow
image = data[0].data
plt.imshow(image, cmap ="hot")      


#now try displaying a bigger figure
#and a color bar
plt.figure(figsize=(15,10.5))
plt.imshow(image)
plt.colorbar()

#now display using a different color map
#and experiment with different color maps
plt.figure(figsize=(15,7.5))
plt.imshow(image, cmap="hot")
plt.colorbar()

#now try zooming in
plt.figure(figsize=(15,7.5))
plt.imshow(image[350:650,350:650], origin="upper", cmap="hot")
plt.colorbar()