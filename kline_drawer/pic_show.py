import cv2


image = cv2.imread("B.png")
image = cv2.resize(image, (400, 100))
img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow("fgh", img_gray)
cv2.waitKey(0)