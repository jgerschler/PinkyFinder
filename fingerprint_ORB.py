import cv2

img = cv2.imread('thinned.png', 0)

orb = cv2.ORB_create(10)
keypoints = orb.detect(img, None)
keypoints, descriptors = orb.compute(img, keypoints)

kp_img = cv2.drawKeypoints(img, keypoints, None, color=(0,255,0), flags=0)


cv2.imshow('ORB', kp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
