#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 04:29:11 2019

@author: abhishek
"""

import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)
while True:
    _, frame = cap.read()
    blurred_frame = cv.GaussianBlur(frame, (5, 5), 0)
    hsv = cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)
    lower_blue = np.array([38, 86, 0])
    upper_blue = np.array([121, 255, 255])
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    cnts,_ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for contour in cnts:
        cv.drawContours(frame, contour, -1, (0, 255, 0), 3)
        cv.imshow("Frame", frame)
    cv.imshow("Mask", mask)
    key = cv.waitKey(1)
    if key == 27:
        break
        
cap.release()
cv.destroyAllWindows()