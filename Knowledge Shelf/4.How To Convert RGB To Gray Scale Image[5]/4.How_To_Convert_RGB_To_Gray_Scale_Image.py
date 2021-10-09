import cv2

img=cv2.imread('lena.jpg')
cv2.imshow('Original Image',img)
cv2.waitKey(0)

gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('Gray Scale Image',gray_img)
cv2.waitKey(0)

img2=cv2.imread('lena.jpg',0)
cv2.imshow('Gray Scale` Image',img2)
cv2.waitKey(0)

cv2.destroyAllWindows()