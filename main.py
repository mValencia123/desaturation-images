import cv2 as cv
import numpy as np

img = cv.imread('test-2.jpg')

cv.imshow('img',img)

rows = np.size(img,axis=0)
cols = np.size(img,axis=1)
imgDesa = np.zeros([rows,cols])
imgDesaMin = np.zeros([rows,cols])
imgDesaMax = np.zeros([rows,cols])
for x in range(rows):
    for y in range(cols):
        imgDesaMin[x,y] = np.double(min(img[x,y,0],img[x,y,1],img[x,y,2]))
        imgDesaMax[x,y] = np.double(max(img[x,y,0],img[x,y,1],img[x,y,2]))
        pixel = (np.double(max(img[x,y,0],img[x,y,1],img[x,y,2]) + min(img[x,y,0],img[x,y,1],img[x,y,2]))) / 2
        imgDesa[x,y] = pixel
imgDesa = np.uint8(imgDesa)
imgDesaMin = np.uint8(imgDesaMin)
imgDesaMax = np.uint8(imgDesaMax)
cv.imshow('imgDesa',imgDesa)
cv.imshow('imgDesaMin',imgDesaMin)
cv.imshow('imgDesaMax',imgDesaMax)
cv.waitKey(0) 