import cv2 as cv

original_image = cv.imread('../images/tree.png')

negative_image = 255 - original_image

cv.imshow("grayscale image", original_image)

cv.imshow("negative image", negative_image)

cv.waitKey(0)