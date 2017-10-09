import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('prints\\101_1.tif', 0)

ret, threshold = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

plt.subplot(1, 1, 1)
plt.imshow(threshold, 'gray')
plt.show()

print("Done!")
