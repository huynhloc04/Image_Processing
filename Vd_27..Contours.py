
#   Good link: https://medium.com/analytics-vidhya/opencv-findcontours-detailed-guide-692ee19eeb18
#              Hierarchy explaination: https://docs.opencv.org/master/d9/d8b/tutorial_py_contours_hierarchy.html

# import cv2
# img_st = cv2.imread("OpenCV.png")
# img_gr = cv2.cvtColor(img_st, cv2.COLOR_BGR2GRAY)
# _, Thresh = cv2.threshold(img_gr, 200, 255, cv2.THRESH_BINARY)
# contours, _ = cv2.findContours(Thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# #   Contours is a List of all the contours in the image. Each individual contour is a numpy arr of (x,y) coordinates of boundary of the object
# #   Hierarchy is the   output vector which is containing information about image topology
# print("Number of contours", str(len(contours)))
# #   Draw the cotours on image
# cv2.drawContours(img_st, contours, -1, (0,255,255), 2)  # argument: -1 => Show all contours
# #   img_st: ảnh nguồn cần vẽ contour
# #   contour: List các contour trong hàm tìm contour
# #   -1: Số contour cần hiển thị
# #   (0,255,0): Màu sắc của contour
# #   2: Độ dày của nét contour
# cv2.imshow("Original_Image", img_st)
# cv2.imshow("OpenCV_Logo", Thresh)
# cv2.waitKey()
# cv2.destroyAllWindows()



# import cv2
# import numpy as np
# img = cv2.imread("WorldMap.jpg")
# black = np.zeros((852,1000,3), np.uint8)
# print(img.shape)
# img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# _, Thresh = cv2.threshold(img_gr, 200, 255, cv2.THRESH_BINARY)
# cv2.imshow("Threshold_Image", Thresh)
# contours, _ = cv2.findContours(Thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(black, contours, -1, (0,255,0), 1)
# cv2.imshow("Image", img)
# cv2.imshow("Black_Contours", black)
# cv2.waitKey()
# cv2.destroyAllWindows()


#============ Show the image on the BLACK Background ================

# import cv2
# import numpy as np
# Camera_ID = 0
# cap = cv2.VideoCapture(Camera_ID)
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret:
#         frame_gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         black = np.zeros((480,640,3), np.uint8)
#         _, Thresh = cv2.threshold(frame_gr, 130, 255, cv2.THRESH_BINARY)
#         contours, _ = cv2.findContours(Thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#         cv2.drawContours(black, contours, -1, (0,255,0), 1)
#         cv2.imshow("Image", black)
#     if cv2.waitKey(10) == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()

#   ==================  Using_Trackbar contours to detect Object ============
# import cv2
# import numpy as np

# def nothing():
#     pass

# Camera_ID = 0
# cap = cv2.VideoCapture(Camera_ID)
# cv2.namedWindow("Tracking")
# cv2.createTrackbar("L_H", "Tracking", 0, 179, nothing)
# cv2.createTrackbar("L_S", "Tracking", 0, 255, nothing)
# cv2.createTrackbar("L_V", "Tracking", 0, 255, nothing)
# cv2.createTrackbar("U_H", "Tracking", 0, 179, nothing)
# cv2.createTrackbar("U_S", "Tracking", 0, 255, nothing)
# cv2.createTrackbar("U_V", "Tracking", 0, 255, nothing)
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret:
#         HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         L_H = cv2.getTrackbarPos("L_H", "Tracking")
#         L_S = cv2.getTrackbarPos("L_S", "Tracking")
#         L_V = cv2.getTrackbarPos("L_V", "Tracking")
#         U_H = cv2.getTrackbarPos("U_H", "Tracking")
#         U_S = cv2.getTrackbarPos("U_S", "Tracking")
#         U_V = cv2.getTrackbarPos("U_V", "Tracking")
#         Lower_Color = np.array([L_H, L_S, L_V])
#         Upper_Color = np.array([U_H, U_S, U_V])
#         Mask = cv2.inRange(HSV, Lower_Color, Upper_Color)
#         cv2.imshow("Image_Mask", Mask)
#         contours, _ = cv2.findContours(Mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#         for cnt in contours:
#             epsilon = 0.01*cv2.arcLength(cnt, True)
#             approx = cv2.approxPolyDP(cnt, epsilon, True)
#             if cv2.contourArea(cnt) > 1000:
#                 cv2.drawContours(frame, [approx], 0, (0,255,0), 3)
#         cv2.imshow("Image", frame)
#     if cv2.waitKey(10) == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()


import cv2
img_st = cv2.imread("OpenCV.png")
img_gr = cv2.cvtColor(img_st, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img_gr, (5,5), .5)
_, Thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(Thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_st, contours, -1, (0, 255, 0), 2)
print(cv2.contourArea(contours[9], oriented = True))
cv2.imshow("Image", img_st)
cv2.imshow("Blur", blur)
cv2.imshow("Thresh", Thresh)

cv2.waitKey()
cv2.destroyAllWindows()