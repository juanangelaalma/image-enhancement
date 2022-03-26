import cv2 as cv
import numpy as np

original_image = cv.imread("../images/lovebird.jpg")

grayscale_image = original_image.copy()

for i in range(original_image.shape[0]):
  for j in range(original_image.shape[1]):
    lm = (int(np.max(original_image[i][j])) + int(np.min(original_image[i][j]))) / 2
    grayscale_image[i][j] = lm

cv.imshow("original image", original_image)
cv.imshow("grayscale image", grayscale_image)

cv.waitKey(0)