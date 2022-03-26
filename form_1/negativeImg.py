import cv2 as cv

original_image = cv.imread('../images/tree.png')

negative_image = original_image.copy()

negative_image = 255 - original_image

for i in range(original_image.shape[0]):
  for j in range(original_image.shape[1]):
    r, g, b = original_image[i][j]
    negative_image[i][j] = 255 - original_image[i][j]


cv.imshow("grayscale image", original_image)

cv.imshow("negative image", negative_image)

cv.waitKey(0)