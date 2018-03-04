import cv2
import numpy as np
import timeit

img = cv2.imread('thinned.png', 0)

surf = cv2.xfeatures2d.SURF_create(4000)
keypoints, descriptors = surf.detectAndCompute(img, None)
kp_img = cv2.drawKeypoints(img, keypoints, None, (0, 255, 0))

##img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)


cv2.imshow('SURF', kp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
