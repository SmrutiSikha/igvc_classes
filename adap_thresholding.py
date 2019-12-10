#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 23:08:20 2019

@author: abhishek
"""

import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np
image=cv.imread('img.jpg')
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
(h,thr)=cv.threshold(gray,50,255,cv.THRESH_BINARY)
plt.imshow(thr)
(h_,thr_inv)=cv.threshold(gray,50,255,cv.THRESH_BINARY_INV)
plt.imshow(thr_inv)
cv.bitwise_and(gray,thr_inv)
plt.imshow(gray)
thres=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,21,4)
plt.imshow(thres)