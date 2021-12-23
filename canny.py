import cv2
import os
import numpy as np

name = "img/ng_station4_10pin_pin_2484.jpg"
size =  (256,256)
img = cv2.resize(cv2.imread(name), size)
edges = cv2.Canny(img,100,200)

print(img.shape)

cv2.imshow(name , edges)
cv2.waitKey(0)
