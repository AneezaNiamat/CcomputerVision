import cv2

#Create the argument parser and parse the arguments

#read the image

image=cv2.imread('cameramannoise.jpg')
#apply the 3*3 median filter on the image
processed_image=cv2.medianBlur(image,3)
#display image
cv2.imshow('median Filter Processing', processed_image)
#save image to disk
cv2.imwrite('processed_image.png', processed_image)
#pause the execution of the script until 0 key on the keyboard is present
cv2.waitKey(0)