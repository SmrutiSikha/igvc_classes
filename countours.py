#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 00:08:58 2019

@author: abhishek
"""

import cv2 as cv
import matplotlib.pyplot as plt
image=cv.imread("image.png")
img=image.copy()
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
canny=cv.Canny(gray,30,150)
plt.imshow(canny)
 cnts,_ = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
for c in range(len(cnts)):
    cv.drawContours(img, cnts, c, (255, 0, 0), 3)
    cv.imshow("cnts", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
cv.destroyAllWindows()
for c in cnts:
    cv.drawContours(img, c, -1, (0, 255, 0), 2)
    cv.imshow("cnts", img)
    cv.waitKey(0)
    cv.destroyAllWindows()