# rumus s = cr^y


# asumsi c = 1 && y = 0.2

import cv2 as cv
import numpy as np

original_image = cv.imread("../images/lovebird.jpg")

powerlaw_image = original_image.copy()

c = 1
y = 0.8

# s = cr^y
for i in range(original_image.shape[0]):
  for j in range(original_image.shape[1]):
    r, g, b = original_image[i][j]
    powerlaw_image[i][j] = c * (powerlaw_image[i][j]**y)

cv.imshow("original image", original_image)
cv.imshow("power law image", powerlaw_image)
cv.waitKey(0)