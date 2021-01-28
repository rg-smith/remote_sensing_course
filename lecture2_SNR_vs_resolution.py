import os
#import scipy
import matplotlib.image as img
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

def multilook(raster,looks):
    for kk in range(raster.shape[2]):
        raster[:,:,kk]=ndimage.generic_filter(np.squeeze(raster[:,:,kk]), np.nanmean, size=looks, mode='constant', cval=np.NaN)
        raster[:,:,kk]=raster[:,:,kk]/np.nanmax(raster[:,:,kk])
    return(raster)


os.chdir('C:/Users/smithryang/Box Sync/Classes/Remote_sensing/remote_sensing_class/2021/Lectures')
#dat=scipy.misc.imread('football_field.jpg')
dat=img.imread('football_field.jpg')
dat=dat[1::2,1::2,:]
noise=np.random.uniform(low=0,high=1000,size=dat.shape)
dat2=dat+noise
dat2=dat2/np.max(dat2)
plt.figure();
plt.subplot(2,2,1)
plt.imshow(dat);
plt.subplot(2,2,2);
plt.imshow(dat2)
dat_multilook=multilook(dat2,21)
plt.subplot(2,2,3)
plt.imshow(dat_multilook)
