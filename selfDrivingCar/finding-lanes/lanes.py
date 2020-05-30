import cv2

image = cv2.imread('test_image.jpg')
cv2.imshow('result', image)
cv2.waitKey(0)


#echo /usr/local/opt/opencv/lib/python3.7/site-packages >>/usr/local/lib/python3.7/site-packages/opencv3.pth
