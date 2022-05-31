# import cv2
# import numpy as np
# img = cv2.imread("Building.jpg")
# img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray_Image", img_gr)
# Gblur = cv2.GaussianBlur(img_gr, (5,5), 0)
# cv2.imshow("Gaussian_Image", Gblur)
# edge = cv2.Canny(Gblur, 70, 100)
# cv2.imshow("Image_Canny", edge)
# lines = cv2.HoughLinesP(edge, 1, np.pi/180, 100, minLineLength = 60, maxLineGap = 15)
# #       100 => Threshold    : Những Line nào có số điểm lớn hơn 100 mới đc lấy
# #       minLineLength = x  : Những cái line nào có chiều dài nhỏ hơn x sẽ bị từ chối
# #       maxLineGap = y     : Trên Line có bất kì 2 điểm nào mà khoảng cách giữa hai điểm đó lớn hơn y thì sẽ ko đc vẽ Line. 
# #   (Cụ thể trong ảnh Sodoku có những Line chạy ra cả ngoài biên của bàn cờ, những đoạn dư đó sẽ bị lược bỏ. Bởi vì kc giữa hai điểm thuộc bàn cờ và mép ảnh > y)
# for line in lines:
#     x1, y1, x2, y2 = line[0]
#     cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 1)
# cv2.imshow("Hough_Transform",img)
# cv2.waitKey()
# cv2.destroyAllWindows()


#    =============================== Probabilistic Hough Transform by using "VIDEO" ===============================

import cv2
import numpy as np

# def nothing():
#     pass

cap = cv2.VideoCapture("Highway.mp4")
# cv2.namedWindow("Tracking")
# cv2.createTrackbar("minVal", "Tracking", 0, 900, nothing)
# cv2.createTrackbar("maxVal", "Tracking", 0, 900, nothing)
while(cap.isOpened()):
    ret, frame = cap.read()
    if cv2.waitKey(10) == ord("q"):
        break
    if ret:
        # minVal = cv2.getTrackbarPos("minVal", "Tracking")
        # maxVal = cv2.getTrackbarPos("maxVal", "Tracking")
        img_gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(img_gr, 198, 720)
        #cv2.imshow("Origin_Video", frame)
        #cv2.imshow("Edge_Video", edge)
        lines = cv2.HoughLinesP(edge, 1, np.pi/180, 25, minLineLength = 15, maxLineGap = 8)
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)
        cv2.imshow("Hough_Transform", frame)
cap.release()
cv2.destroyAllWindows()