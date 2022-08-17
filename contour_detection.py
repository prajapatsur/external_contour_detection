import cv2
import numpy as np

img = cv2.imread('tree.jfif')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,binary = cv2.threshold(img_gray,195,255,cv2.THRESH_BINARY)

contours1,heirarchy1 = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print(len(contours1))

cv2.drawContours(img,contours1,-1,(255,100,0),2,cv2.LINE_AA) 

cv2.imshow('Binary image',binary)
cv2.imshow('Contours1',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
