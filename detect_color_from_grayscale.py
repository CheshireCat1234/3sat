# import the necessary packages
import numpy as np
import cv2

# load the image
image = cv2.imread('6.png')

# remove red and blue channels
image[:, :, 2] = np.zeros([image.shape[0], image.shape[1]])
image[:, :, 0] = np.zeros([image.shape[0], image.shape[1]])

# convert to grayscale and count pixels
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 34, 0, cv2.THRESH_TOZERO_INV)

# calculate forests
non_zero_pixels = cv2.countNonZero(thresh)
print('The percentage of forests in the image is {}'.format(non_zero_pixels / thresh.size * 100))

# show the images
cv2.imshow('images', thresh)
cv2.waitKey(0)
