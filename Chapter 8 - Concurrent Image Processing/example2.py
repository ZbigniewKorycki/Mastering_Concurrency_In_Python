import cv2

im = cv2.imread('ship.png')
gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_im)
cv2.waitKey(0)

print(gray_im)
print('Type:', type(gray_im))
print('Shape:', gray_im.shape)

cv2.imwrite('gray_ship.png', gray_im)

print('Done')

