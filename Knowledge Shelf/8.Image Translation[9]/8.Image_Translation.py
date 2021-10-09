import cv2
import numpy as np

img=cv2.imread('lena.jpg')

# store height and width of image 

height,width=img.shape[:2]
print(height)
print(width)

quarter_height,quarter_width=height/3,width/3
print(quarter_height)
print(quarter_width)

#     |1 0 Tx|
# T=  |1 0 Tx|

# T is Our Translation Matrix

T=np.float32([[1,0,quarter_width],
            [0,1,quarter_height]])
print(T)

# We use warpAffine Transformation to shift the image
img_translation=cv2.warpAffine(img,T,(width,height))

cv2.imshow('Original Image',img)
cv2.imshow('Translation Image',img_translation)

cv2.waitKey(0)
cv2.destroyAllWindows()