import cv2
img = cv2.imread("1.jpg")
#img = cv2.resize(img,(256,256))
blur = cv2.blur(img,(10,10))
cv2.imwrite("Blurred_Image.jpg",blur)