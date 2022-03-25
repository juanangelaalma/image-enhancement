# rumus s = cr^y


# asumsi c = 1 && y = 0.2

import cv2 as cv
import numpy as np

original_image = cv.imread("../images/birds.jpg")
gray_scale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

c = 1
y = 1.1

# s = cr^y
powerlaw_image = (c * original_image) ** y

# float value will be convert to int 
powerlaw_image = np.array(powerlaw_image, dtype = np.uint8)

cv.imshow("power law image", powerlaw_image)
cv.waitKey(0)