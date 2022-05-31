
#   - What is Object_Tracking: When we use object detection, it detects an object in every frame. So, basically it is a series of repeated 
# detections. On the other hand, object tracking only requires object detection in the first frame. After that detection, the algorithm has 
# enough information about the object. It learns about the appearance of the object, the location in the previous frame, and the direction 
# and the velocity of its motion. Then, the algorithm can use all this information to predict the location of the object in the next frame.


#   ================================================= MEAN_SHIFT =============================================


#   Link: https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_mean_shift_tracking_segmentation.php
#         https://docs.opencv.org/master/d7/d00/tutorial_meanshift.html


# import cv2
# CameraID = 0
# cap = cv2.VideoCapture(CameraID)
# ROI = cv2.imread("ROI_MeanShf.jpg")
# ROI_HSV = cv2.cvtColor(ROI, cv2.COLOR_BGR2HSV)
# ROI_Hist = cv2.calcHist([ROI_HSV], [0, 1], None, [180, 256], [0, 180, 0, 256])
# print(ROI_Hist)
# #      Use Image Normalization to remove noise from the picture.With the help of Image Normalization, we can remove high-frequency 
# #   noise and very low noise from the image which is really helpful
# #   LINK: https://www.codespeedy.com/normalizing-an-image-in-opencv-python/

# #   ============================== Sử dụng MOUSE_EVENT để tìm ROI của ảnh ban đầu ================================
# # def Mouse_Back(event, x, y, flags, params):
# #     if event ==cv2.EVENT_LBUTTONDOWN:
# #         font = cv2.FONT_HERSHEY_COMPLEX_SMALL
# #         Str = f"({x}, {y})"
# #         cv2.putText(img, Str, (x,y), font, 0.5, (0,0,255), 1, cv2.LINE_AA)
# #         cv2.imshow("First_Image", img)

# term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TermCriteria_COUNT, 10, 1)
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret:
#         frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         Mask = cv2.calcBackProject([frame_HSV], [0, 1], ROI_Hist, [0, 180, 0, 256], 1)
#         _, Track_Win = cv2.meanShift(Mask, (227,177,454,298), term_criteria)
#         (x, y, w, h) = Track_Win
#         cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
#         cv2.imshow("Mask_Detect", frame)
#     if cv2.waitKey(10) == ord("q"):
#         break
# # cv2.imshow("First_Image", img)
# # cv2.setMouseCallback("First_Image", Mouse_Back)
# cap.release()
# cv2.waitKey()
# cv2.destroyAllWindows()





#   ================================================= CAM_SHIFT =============================================

import cv2
import numpy as np 
Mask_Cover = cv2.imread("ROI_MeanShf.jpg")
HSV_Cover = cv2.cvtColor(Mask_Cover, cv2.COLOR_BGR2HSV)
Cover_Hist = cv2.calcHist([HSV_Cover], [0, 1], None, [180, 256], [0, 180, 0, 256])
cap = cv2.VideoCapture(0)
Init_Win = (227, 452, 225, 119)
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        Mask = cv2.calcBackProject([HSV_frame], [0, 1], Cover_Hist, [0, 180, 0, 256], 1)
        ret, Track_Win = cv2.CamShift(Mask, Init_Win, term_crit)
        # (x, y, w, h) = Track_Win
        # pst = np.array([
        #     [x, y],
        #     [x+w, y],
        #     [x+w, y+h],
        #     [x, y+h]
        #                ])
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        cv2.polylines(frame, [pts], True, (0, 255, 0), 2)         
        cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()