import cv2 as cv

originalImage = cv.imread('../images/tree.png')

negativeImage = 255 - originalImage

cv.imshow("grayscale image", originalImage)

cv.imshow("negative image", negativeImage)

cv.waitKey(0)