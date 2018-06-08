import cv2
import numpy as np
import time

img = cv2.imread('thinned.png', 0)

t0 = time.clock()
corners = cv2.goodFeaturesToTrack(img, 10, 0.01, 3, True)
t1 = time.clock()
corners = np.int0(corners)

img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 5, (0, 69, 255), 1)

print(t1-t0)

cv2.imshow('Shi-Tomasi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()