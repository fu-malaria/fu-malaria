import numpy as np
import cv2

im = cv2.imread('malaria1.jpg')

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,200,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im,contours,-1,(0,255,0),1)

cv2.imshow('image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
