import cv2
import numpy as np
import timeit

img = cv2.imread('thinned.png', 0)

sift = cv2.xfeatures2d.SIFT_create(10)
keypoints = sift.detect(img, None)
kp_img = cv2.drawKeypoints(img, keypoints, None, (0, 255, 0))

##img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)


cv2.imshow('SIFT', kp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
