# rumus s = c log(1 + r)
# c = L / log(1 + r)
import cv2 as cv
import numpy as np

original_image = cv.imread("../images/tree.png")

# method of log tranformation
c = 255 / np.log(1 + np.max(original_image))
log_image = c * np.log(original_image + 1)

# float value will be convert to int 
log_image = np.array(log_image, dtype = np.uint8)

cv.imshow("grayscale image", original_image)

cv.imshow("log image", log_image)

cv.waitKey(0)