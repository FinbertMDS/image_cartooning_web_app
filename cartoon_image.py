# -*- coding: utf-8 -*-
"""
Created on Wed May 20 01:05:53 2020

@author: ASUS
"""
import cv2
import numpy as np 
from PIL import Image


def cartoonization (img, cartoon):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    if cartoon == "Pencil Sketch":
        
        value = 250.0
        kernel = 25


        gray_blur = cv2.GaussianBlur(gray, (kernel, kernel), 0)

        cartoon = cv2.divide(gray, gray_blur, scale=value)

    if cartoon == "Detail Enhancement":
        
       
        smooth = 5
        kernel = 3
        edge_preserve = 0.5
        
        gray = cv2.medianBlur(gray, kernel) 
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
 										cv2.THRESH_BINARY, 9, 9) 
    
        color = cv2.detailEnhance(img, sigma_s=smooth, sigma_r=edge_preserve)
        cartoon = cv2.bitwise_and(color, color, mask=edges) 

    if cartoon == "Pencil Edges":
    
        kernel = 25
        laplacian_filter = 3
        noise_reduction = 150
        
        gray = cv2.medianBlur(gray, kernel) 
        edges = cv2.Laplacian(gray, -1, ksize=laplacian_filter)

        
        edges_inv = 255-edges
    
        dummy, cartoon = cv2.threshold(edges_inv, noise_reduction, 255, cv2.THRESH_BINARY)
        

    if cartoon == "Bilateral Filter":
        
        
       
        smooth = 5
        kernel = 3
        edge_preserve = 50
       
        gray = cv2.medianBlur(gray, kernel) 
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
 										cv2.THRESH_BINARY, 9, 9)
    
        color = cv2.bilateralFilter(img, smooth, edge_preserve, smooth) 
        cartoon = cv2.bitwise_and(color, color, mask=edges) 

    return cartoon

###############################################################################

file="./image/original.jpg"
image = Image.open(file)
img = np.array(image)

option = "Bilateral Filter"
cartoon = cartoonization(img, option)
cv2.imwrite('./myphoto.jpeg', cartoon)
