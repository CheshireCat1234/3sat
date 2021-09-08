# import the necessary packages
import numpy as np
import cv2

# load the image
image = cv2.imread('6.png')

# define the list of boundaries
lower = np.array([1, 1, 1], dtype="uint8")
upper = np.array([40, 60, 55], dtype="uint8")

# find the colors within the specified boundaries and apply the mask
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask=mask)

# convert to grayscale and count pixels
gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 255, 0, cv2.THRESH_TOZERO_INV)

# calculate forests
non_zero_pixels = cv2.countNonZero(thresh)
print('The percentage of forests in the image is {}'.format(non_zero_pixels / thresh.size * 100))

# show the images
cv2.imshow('images', thresh)
cv2.waitKey(0)
