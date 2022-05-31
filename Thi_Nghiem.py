import cv2
import numpy as np 

def nothing():
    pass

img_st = cv2.imread("Thi_Nghiem.jpg")
img = cv2.resize(img_st, (512,512))
#cv2.imshow("Image", img)
img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Gblur = cv2.GaussianBlur(img_gr, (5,5), 0)

#   ======================= Create a Trackbar ===========================
# cv2.namedWindow("Tracking")
# cv2.createTrackbar("minVal", "Tracking", 0, 500, nothing)
# cv2.createTrackbar("maxVal", "Tracking", 0, 500, nothing)
# while True:
#     if cv2.waitKey(10) == ord("q"):
#         break
#     minVal = cv2.getTrackbarPos("minVal", "Tracking",)
#     maxVal = cv2.getTrackbarPos("maxVal", "Tracking")
#     edge = cv2.Canny(Gblur, minVal, maxVal)
#     cv2.imshow("Image", edge)

Circles = cv2.HoughCircles(Gblur, cv2.HOUGH_GRADIENT, 1, 10, param1 = 90, param2 = 10, minRadius = 0, maxRadius = 10)
print(Circles[0])
if Circles is not None:
    Circles = np.round(Circles).astype("int")
    for x, y, r in Circles[0]:
        cv2.circle(img, (x, y), r, (0,255,0), 2)
    cv2.imshow("Image", img)
cv2.waitKey()
cv2.destroyAllWindows()
