import cv2
import numpy as np
# Load citra grayscale
img = cv2.imread('../images/birds.jpg', 0)

# Lakukan iterasi setiap piksel dan ubah nilai piksel kedalam binary menggunakan fungsi np.ninary_repr()
binary_img = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        binary_img.append(np.binary_repr(img[i][j], width=8))  # width = no. of bits

# Lakukan iterasi dari setiap string yang merepresentasikan nilai biner piksel
bit_eight_img = (np.array([int(i[0]) for i in binary_img], dtype=np.uint8) * 128).reshape(img.shape[0], img.shape[1])
bit_seven_img = (np.array([int(i[1]) for i in binary_img], dtype=np.uint8) * 64).reshape(img.shape[0], img.shape[1])
bit_six_img = (np.array([int(i[2]) for i in binary_img], dtype=np.uint8) * 32).reshape(img.shape[0], img.shape[1])
bit_five_img = (np.array([int(i[3]) for i in binary_img], dtype=np.uint8) * 16).reshape(img.shape[0], img.shape[1])
bit_four_img = (np.array([int(i[4]) for i in binary_img], dtype=np.uint8) * 8).reshape(img.shape[0], img.shape[1])
bit_three_img = (np.array([int(i[5]) for i in binary_img], dtype=np.uint8) * 4).reshape(img.shape[0], img.shape[1])
bit_two_img = (np.array([int(i[6]) for i in binary_img], dtype=np.uint8) * 2).reshape(img.shape[0], img.shape[1])
bit_one_img = (np.array([int(i[7]) for i in binary_img], dtype=np.uint8) * 1).reshape(img.shape[0], img.shape[1])

# Concatenate citra bit plane sehingga mudah untuk ditampilkan menggunakan cv2.hconcat()
sliced_img_r = cv2.hconcat([bit_eight_img, bit_seven_img, bit_six_img, bit_five_img])
sliced_img_v = cv2.hconcat([bit_four_img, bit_three_img, bit_two_img, bit_one_img])

# Vertically concatenate
sliced_img = cv2.vconcat([sliced_img_r, sliced_img_v])
resized_sliced_img = cv2.resize(sliced_img, (960, 540))

# Menampilkan Citra Bit Plane
cv2.imshow('Bit Plane Slicing Image', resized_sliced_img)
cv2.waitKey(0)