# rumus Pout = (Pin - Min) * ( (b - a) / Max - Min ) + a

# Pin = pixel masuk
# Min = min pixel
# Max = max pixel
# b = 255
# a = 0

import cv2 as cv
import numpy as np

original_image = cv.imread("../images/tree.png")

min_pixel = np.min(original_image)
max_pixel = np.max(original_image)
b = 255
a = 0

contrast_image = original_image.copy()

for i in range(original_image.shape[0]):
  for j in range(original_image.shape[1]):
    r, g, b = original_image[i][j]
    contrast_image[i][j] = (original_image[i][j] - min_pixel) * ( (b - a) / (max_pixel - min_pixel) ) + a


cv.imshow("original image", original_image)
cv.imshow("contrast image", contrast_image)

cv.waitKey(0)