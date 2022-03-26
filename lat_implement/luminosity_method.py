import cv2 as cv

original_image = cv.imread("../images/lovebird.jpg")

grayscale_image = original_image.copy()

for i in range(original_image.shape[0]):
  for j in range(original_image.shape[1]):
    r, g, b = original_image[i][j]
    grayscale_image[i][j] = ((21/100 * int(r)) + (71/100 * int(g)) + 7/100(int(b)))

# grayscale_image = np.array(grayscale_image, dtype=np.uint8)
cv.imshow("original image", original_image)
cv.imshow("grayscale image", grayscale_image)

cv.waitKey(0)