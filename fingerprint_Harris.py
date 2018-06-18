import cv2
import numpy as np

img = cv2.imread('thinned.png', 0)

corners = cv2.goodFeaturesToTrack(img, 20, 0.01, 3, True)
corners = np.int0(corners)

img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), 1)

cv2.imwrite('harris.png', img)

cv2.imshow('Harris', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
