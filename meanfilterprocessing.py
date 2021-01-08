# import cv2
# import numpy as np
#
# image=cv2.imread('cameramannoise.jpg')
# kernel=np.ones((3,3), np.float32)/9
# processed_image=cv2.filter2D(image, -1, kernel)
# cv2.imshow('Mean Filter Processing', processed_image)
# cv2.imwrite('processed_image.png', processed_image)
# cv2.waitKey(0)
import cv2
import numpy as np

#read the image
image=cv2.imread('cameranoise.jpg')
#apply the 3*3 mean filter on the image
kernel=np.ones((3, 3), np.float32) / 9
processed_image=cv2.filter2D(image, -1, kernel)
#display image
cv2.imshow('Mean Filter Processing', processed_image)
#save image to disk
cv2.imwrite('processed_image.png', processed_image)
#pause the execution of the script until 0 key on the keyboard is present
cv2.waitKey(0)