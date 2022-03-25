# rumus s = c log(1 + r)
# c = L / log(1 + r)
import cv2 as cv
import numpy as np

originalImage = cv.imread("../images/tree.png")

# method of log tranformation
c = 255 / np.log(1 + np.max(originalImage))
logImage = c * np.log(originalImage + 1)

# float value will be convert to int 
logImage = np.array(logImage, dtype = np.uint8)

cv.imshow("grayscale image", originalImage)

cv.imshow("log image", logImage)

cv.waitKey(0)