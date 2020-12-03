import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ここに画像のファイル',0)
edges = cv2.Canny(img,100,200)

cv2.imshow('output', edges)
cv2.imwrite("output.png", edges)
cv2.waitKey(0)