import cv2 as cv
import numpy as np

#Lage funksjon

image_balls = 'balls.png'

image = cv.imread(image_balls, cv.IMREAD_COLOR)

print(image.shape)

cv.imshow('image', image)

cv.waitKey(0)

cv.destroyAllWindows()