#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 19:10:31 2019

@author: abhishek
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread("img.jpg")
copy=image.copy()
(b,g,r)=image[0,0]
image[0:100,0:100]=(255,255,255)
plt.imshow(copy)
