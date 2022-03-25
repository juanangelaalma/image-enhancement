# rumus Pout = (Pin - Min) * ( (b - a) / Max - Min ) + a

# Pin = pixel masuk
# Min = min pixel
# Max = max pixel
# b = 255
# a = 0

import cv2 as cv
import numpy as np

originalImage = cv.imread("../images/tree.png")

grayScaleImage = cv.cvtColor(originalImage, cv.COLOR_BGR2GRAY)

min_pixel = np.min(grayScaleImage)
max_pixel = np.max(grayScaleImage)
b = 255
a = 0

contrast_image = (grayScaleImage - min_pixel) * ( (b - a) / (max_pixel - min_pixel) ) + a

# float value will be convert to int 
contrast_image = np.array(contrast_image, dtype = np.uint8)

cv.imshow("original image", grayScaleImage)
cv.imshow("contrast image", contrast_image)

cv.waitKey(0)