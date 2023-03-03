import cv2 as cv
import numpy as np

img = cv.imread('test-2.jpg')
img2 = cv.imread('img-leon.jpg')

#cv.imshow('img',img)

rows = np.size(img,axis=0)
cols = np.size(img,axis=1)
# imgDesa = np.zeros([rows,cols])
# imgDesaMin = np.zeros([rows,cols])
# imgDesaMax = np.zeros([rows,cols])
# for x in range(rows):
#     for y in range(cols):
#         imgDesaMin[x,y] = np.double(min(img[x,y,0],img[x,y,1],img[x,y,2]))
#         imgDesaMax[x,y] = np.double(max(img[x,y,0],img[x,y,1],img[x,y,2]))
#         pixel = (np.double(max(img[x,y,0],img[x,y,1],img[x,y,2]) + min(img[x,y,0],img[x,y,1],img[x,y,2]))) / 2
#         imgDesa[x,y] = pixel
# imgDesa = np.uint8(imgDesa)
# imgDesaMin = np.uint8(imgDesaMin)
# imgDesaMax = np.uint8(imgDesaMax)
imgCV = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgCV2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

# cv.imshow('imgDesa',imgDesa)
# cv.imshow('imgDesaMin',imgDesaMin)
# cv.imshow('imgDesaMax',imgDesaMax)
cv.imshow('imgOpenCV',imgCV)
cv.imshow('imgOpenCV2',imgCV2)

# imgCC = np.zeros([rows,cols])
# imgCC2 = np.zeros([rows,cols])
# imgHB = np.zeros([rows,cols])
# imgLB = np.zeros([rows,cols])
# for x in range(rows):
#     for y in range(cols):
#         pixel  = np.double(imgCV[x,y] * 1.5)
#         pixel2 = np.double(imgCV[x,y] * 0.5)
#         pixel3 = np.double(imgCV[x,y] + 100)
#         pixel4 = np.double(imgCV[x,y] - 100)
#         if pixel > 255:
#             pixel = 255
#         if pixel2 > 255:
#             pixel2 = 255
#         if pixel3 > 255:
#             pixel3 = 255
#         if pixel < 0 :
#             pixel = 0
#         imgCC[x,y] = pixel
#         imgCC2[x,y] = pixel2
#         imgHB[x,y] = pixel3
#         imgLB[x,y] = pixel4
# imgCC = np.uint8(imgCC)
# imgCC2 = np.uint8(imgCC2)
# imgHB = np.uint8(imgHB)
# imgLB = np.uint8(imgLB)
# imgCom = 255 - imgCV

# cv.imshow('imgOpenCV contraste',imgCC)
# cv.imshow('imgOpenCV contraste 2',imgCC2)
# cv.imshow('imgOpenCV alto brillo',imgHB)
# cv.imshow('imgOpenCV bajo  brillo',imgLB)
# cv.imshow('imgOpenCV COMPLEMENTO',imgCom)


imgResize = cv.resize(imgCV,[466,521])

imgAux = np.double(0.5 * imgCV2 + 0.5 * imgResize)
imgAux = np.uint8(imgAux)

cv.imshow('imgOpenCV2 combinacion',imgAux)
cv.waitKey(0) 