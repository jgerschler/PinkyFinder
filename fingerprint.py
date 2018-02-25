import cv2
import numpy as np

img = cv2.imread('test.png', 0)
retval, orig_thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)

thresh = (orig_thresh == 0).astype(int)

def pixel_is_black(arr, x, y):# function included for clarity
    if arr[x, y] == 1:
        return True
    return False

def pixel_has_2_to_6_black_neighbors(arr, x, y):
    if (2 <= arr[x, y-1] + arr[x+1, y-1] + arr[x+1, y] + arr[x+1, y+1] +
        arr[x, y+1] + arr[x-1, y+1] + arr[x-1, y] + arr[x-1, y-1] <= 6):
        return True
    return False

def pixel_has_1_white_to_black_neighbor_transition(arr, x, y):
    neighbors = [arr[x, y-1], arr[x+1, y-1], arr[x+1, y], arr[x+1, y+1],
                 arr[x, y+1], arr[x, y+1], arr[x-1, y], arr[x-1, y-1],
                 arr[x, y-1]]
    transitions = sum((a, b) == (0, 1) for a, b in zip(neighbors, neighbors[1:]))
    if transitions == 1:
        return True
    return False
    
def at_least_one_of_P2_P4_P6_is_white(arr, x, y):
    if (arr[x, y-1] and arr[x+1, y] and arr[x, y+1]) == False:
        return True
    return False

def at_least_one_of_P4_P6_P8_is_white(arr, x, y):
    if (arr[x+1, y] and arr[x, y+1] and arr[x-1, y]) == False:
        return True
    return False

def at_least_one_of_P2_P4_P8_is_white(arr, x, y):
    if (arr[x, y-1] and arr[x+1, y] and arr[x-1, y]) == False:
        return True
    return False

def at_least_one_of_P2_P6_P8_is_white(arr, x, y):
    if (arr[x, y-1] and arr[x, y+1] and arr[x-1, y]) == False:
        return True
    return False

thinned_thresh = thresh.copy()
carbon_copy = np.zeros(thresh.shape)

while np.all(carbon_copy == thinned_thresh) != True:
    carbon_copy = thinned_thresh.copy()
    # step one
    pixels_meeting_criteria = []
    for i in range(1, thresh.shape[0] - 1):
        for j in range(1, thresh.shape[1] - 1):
            if (pixel_is_black(thinned_thresh, i, j) and
                pixel_has_2_to_6_black_neighbors(thinned_thresh, i, j) and
                pixel_has_1_white_to_black_neighbor_transition(thinned_thresh, i, j) and
                at_least_one_of_P2_P4_P6_is_white(thinned_thresh, i, j) and
                at_least_one_of_P4_P6_P8_is_white(thinned_thresh, i, j)):
                pixels_meeting_criteria.append((i, j))

    for pixel in pixels_meeting_criteria:
        thinned_thresh[pixel] = 0

    # step two
    pixels_meeting_criteria = []
    for i in range(1, thresh.shape[0] - 1):
        for j in range(1, thresh.shape[1] - 1):
            if (pixel_is_black(thinned_thresh, i, j) and
                pixel_has_2_to_6_black_neighbors(thinned_thresh, i, j) and
                pixel_has_1_white_to_black_neighbor_transition(thinned_thresh, i, j) and
                at_least_one_of_P2_P4_P8_is_white(thinned_thresh, i, j) and
                at_least_one_of_P2_P6_P8_is_white(thinned_thresh, i, j)):
                pixels_meeting_criteria.append((i, j))

    for pixel in pixels_meeting_criteria:
        thinned_thresh[pixel] = 0




##while np.all(thresh == thinned_thresh) != True:
##    iteration()



thresh = (thinned_thresh == 0).astype(np.uint8)
thresh *= 255

print(orig_thresh)
print("XXXXXXXXXXX")
print(thresh)

cv2.imshow('origimage', orig_thresh)
cv2.imshow('thinnedimage', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
