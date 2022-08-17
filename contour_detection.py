import cv2
import numpy as np

img = cv2.imread('tree.jfif')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_canny = cv2.Canny(img_gray,100,200)
img_copy = img.copy()

_,binary = cv2.threshold(img_gray,195,255,cv2.THRESH_BINARY)

contours1,heirarchy1 = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours2,heirarchy2 = cv2.findContours(img_canny,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

print(len(contours1))
print(len(contours2))

cv2.drawContours(img,contours1,-1,(255,100,0),2,cv2.LINE_AA)     #if contousridx is -1, that means it'll show all the contours.
#if contoursidx is 0 then it will show the first contour.
cv2.drawContours(img_copy,contours2,-1,(0,255,0),2,cv2.LINE_AA)
cv2.imshow('Binary image',binary)
cv2.imshow('Contours1',img)
cv2.imshow('Contours2',img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()