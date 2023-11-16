import cv2

im = cv2.imread('ship.png')
gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret, custom_thresh_im = cv2.threshold(gray_im, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('custom_thresh_ship.png', custom_thresh_im)

print('Done')