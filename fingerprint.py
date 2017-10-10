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

def thinning_iteration(img, iter):# iter = 0
    i, j = 0, 0
    marker = np.zeros(img.shape, dtype=np.uint8)
    for i in range(img.shape[0] - 1):
        for j in range(img.shape[1] - 1):
            p2 = img[i - 1, j]
            p3 = img[i - 1, j + 1]
            p4 = img[i, j + 1]
            p5 = img[i + 1, j + 1]
            p6 = img[i + 1, j]
            p7 = img[i + 1, j - 1]
            p8 = img[i, j - 1]
            p9 = img[i - 1, j - 1]

            A = (int(p2 == 0 and p3 == 1) + int(p3 == 0 and p4 == 1) +
                 int(p4 == 0 and p5 == 1) + int(p5 == 0 and p6 == 1) +
                 int(p6 == 0 and p7 == 1) + int(p7 == 0 and p8 == 1) +
                 int(p8 == 0 and p9 == 1) + int(p9 == 0 and p2 == 1))

            B = p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9

            m1 = (p2 * p4 * p6) if iter == 0 else (p2 * p4 * p8)

            m2 = (p4 * p6 * p8) if iter == 0 else (p2 * p6 * p8)

            if (A == 1 and (B >= 2 and B <= 6) and m1 == 0 and m2 == 0):
                marker[i, j] = 1

            
            
            

print("Done!")


#m = np.zeros(size, dtype=np.uint8)
