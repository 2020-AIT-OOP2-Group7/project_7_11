import cv2
import numpy as np

im = cv2.imread('upload_images/inu.jpg')
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayscale_images/opencv_gray_cvtcolr.jpg', im_gray)