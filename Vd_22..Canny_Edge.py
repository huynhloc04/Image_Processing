
#   https://docs.opencv.org/master/da/d22/tutorial_py_canny.html

import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread("Factory.jpg")
cv2.namedWindow("Canny_Bdjust")
cv2.createTrackbar("MIN", "Canny_Bdjust", 0, 500, nothing)
cv2.createTrackbar("MAX", "Canny_Bdjust", 0, 500, nothing)
while True:
    if cv2.waitKey(10) == ord("q"):
        break
    min = cv2.getTrackbarPos("MIN", "Canny_Bdjust")
    max = cv2.getTrackbarPos("MAX", "Canny_Bdjust")
    edges = cv2.Canny(img, min, max)
    cv2.imshow("Image", edges)
cv2.destroyAllWindows()



