21# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:08:44 2019

@author: ibagr
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:45:35 2019

@author: ibagr
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:08:19 2017

@author: a.brooks
based heavily on a laboratory by Kate Follette
"""

#load packages and give them names
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

#read in a .fits file 
#FITS is popular file format used for images in astronomy
data = fits.open('M86 uv.fits')

#.info indicates how many objects are in the list
# there is only one object called PRIMARY
data.info()
#view header information
print(data[0].header)

#make an ordinary 2D array from the image data
#and display using the function imshow
image = data[0].data
plt.imshow(image)    

#now try displaying a bigger figure
#and a color bar
plt.figure(figsize=(15,10.5))
plt.imshow(image)
plt.colorbar()

#now display using a different color map
#and experiment with different color maps
plt.figure(figsize=(15,7.5))
plt.imshow(image, cmap="jet")
plt.colorbar()

#now try zooming in
plt.figure(figsize=(10,10.5))
plt.imshow(image[200:300,200:300], origin="lower", cmap="hot")
plt.colorbar()