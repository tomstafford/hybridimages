#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:22:04 2020

@author: tom

Make hybrid images: https://en.wikipedia.org/wiki/Hybrid_image

Owes a lot to
https://sandipanweb.wordpress.com/2018/07/30/some-image-processing-problems/

Uses conda env in imging.yml

conda env create --name imging --file imging.yml

"""

import socket #to get host machine identity
import os # for joining paths and filenames sensibly

#test which machine we are on and set working directory
if 'tom' in socket.gethostname():
    os.chdir('/home/tom/t.stafford@sheffield.ac.uk/A_UNIVERSITY/toys/hybrid/')
else:
    print("I don't know where I am! ")
    print("Maybe the script will run anyway...")



from skimage.io import imread, imsave
from skimage.color import rgb2gray
from skimage.transform import resize
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt #plotting


#import images as grayscale

im1 = rgb2gray(imread('in/taylor900.jpg'))
im2 = rgb2gray(imread('in/kanye.jpg'))
#im1 = rgb2gray(imread('in/olaf.png'))
#im2 = rgb2gray(imread('in/elsa.png'))
#im1 = rgb2gray(imread('in/oname.png'))
#im2 = rgb2gray(imread('in/ename.png'))


showing=False


if (im1.shape[0] != im2.shape[0]) & (im1.shape[1] != im2.shape[1]):
    print("images different sizes - this wont' work")
    #im2=resize(im2,[550,550]) #resizing code


im_low_freqs= gaussian_filter(im1, sigma=12) #(5,5,1) #high pass filter
im_hig_freqs= 1 - (im2 - gaussian_filter(im2, sigma=5)) #(5,5,1) #get high pass filter by simply substracting low freqs

if showing:
    #displays in interactive console
    plt.figure(figsize=(20,20))
    plt.imshow(im_hig_freqs)                   
    plt.show()

# combine images- simply by adding grayscale values
hybrid=(im_hig_freqs+im_low_freqs)

if showing:
    plt.figure(figsize=(20,20))
    plt.imshow(hybrid)
    plt.show()

#save output
imsave('hybrid.jpg',hybrid)


