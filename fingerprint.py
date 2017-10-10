import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('prints\\101_1.tif', 0)

ret, threshold = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

threshold = cv2.bitwise_not(threshold)# invert image

plt.subplot(1, 1, 1)
plt.imshow(threshold, 'gray')
plt.show()

print(img.shape)
print(img.size)

def thinning_iteration(img, iter):
    i, j = 0, 0
    marker = np.zeros(img.shape, dtype=np.uint8)
    for i in range(img.shape[0] - 1):
        for j in range(img.shape[1] - 1):
            pass
            

print("Done!")


#m = np.zeros(size, dtype=np.uint8)
