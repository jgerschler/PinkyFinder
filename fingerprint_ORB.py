import cv2
import time

img = cv2.imread('thinned.png', 0)

t0 = time.clock()
orb = cv2.ORB_create(10)
keypoints = orb.detect(img, None)
keypoints, descriptors = orb.compute(img, keypoints)
t1 = time.clock()

print(t1-t0)

kp_img = cv2.drawKeypoints(img, keypoints, None, color=(0,255,0), flags=0)


cv2.imshow('ORB', kp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
