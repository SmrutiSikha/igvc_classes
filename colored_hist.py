#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:18:57 2019

@author: abhishek
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
image = cv.imread("img.jpg")
plt.imshow(image)
chans=cv.split(image)
colors=("b","g","r")
plt.figure()
plt.title("'flattenend'color histogrm")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for (chan,color) in zip(chans,colors):
 hist=cv.calcHist([chan],[0],None,[256],[0,256])
 plt.plot(hist,color=color)
 plt.xlim([0,256])           