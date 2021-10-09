import cv2

img=cv2.imread('lena.jpg')
cv2.imshow('Output',img)

print(img.shape)
print('Height Pixel Values:',img.shape[0])
print('Width Pixel Values:',img.shape[1])

cv2.waitKey(0)
cv2.destroyAllWindows()