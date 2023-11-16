import cv2

im = cv2.imread('./ship.png')
cv2.imshow('Test', im)
cv2.waitKey(0)

print(im)
print('Type:', type(im))
print('Shape:', im.shape)
print('Top-left pixel:', im[0, 0])

print('Done')
