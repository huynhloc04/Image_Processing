
#   Object Detection and Object Tracking using HSV color

#   https://docs.opencv.org/3.4/da/d97/tutorial_threshold_inRange.html

#   How to choose the correct lower and upper HSV color to use in cv2.inRange() funtion
#  https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv/48367205#48367205

#   Example: https://stackoverflow.com/questions/32774956/explain-arguments-meaning-in-res-cv2-bitwise-andimg-img-mask-mask

# import cv2
# import numpy as np

# def nothing(x):
#     print(x)

# cv2.namedWindow("Trackbar")
# cv2.createTrackbar("L_H", "Trackbar", 0, 255, nothing)
# cv2.createTrackbar("L_S", "Trackbar", 0, 255, nothing)
# cv2.createTrackbar("L_V", "Trackbar", 0, 255, nothing)
# cv2.createTrackbar("U_H", "Trackbar", 255, 255, nothing)
# cv2.createTrackbar("U_S", "Trackbar", 255, 255, nothing)
# cv2.createTrackbar("U_V", "Trackbar", 255, 255, nothing)

# while True:
#     img_st = cv2.imread("Color_Ball.png")
#     img = cv2.resize(img_st, (400,512))
#     HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     if cv2.waitKey(10) == ord("q"):
#         break
#     U_H = cv2.getTrackbarPos("U_H", "Trackbar")
#     U_S = cv2.getTrackbarPos("U_S", "Trackbar")
#     U_V = cv2.getTrackbarPos("U_V", "Trackbar")
#     L_H = cv2.getTrackbarPos("L_H", "Trackbar")
#     L_S = cv2.getTrackbarPos("L_S", "Trackbar")
#     L_V = cv2.getTrackbarPos("L_V", "Trackbar")
#     Lower_Blue = np.array([L_H, L_S, L_V])
#     Upper_Blue = np.array([U_H, U_S, U_V])
#     #      When you use "mask" on any image then any "pixel" of that image is whose value is in between "LB and UB" 
#     #   will be set to 255(white) otherwise it will be 0(black).
#     mask = cv2.inRange(HSV, Lower_Blue, Upper_Blue)
#     rlts = cv2.bitwise_and(img, img, mask = mask)
#     cv2.imshow("First_Image", img)
#     cv2.imshow("Mask_Image", mask)
#     cv2.imshow("Result_Image", rlts)
# cv2.destroyAllWindows()


#   ============================= OBJECT_TRACKING with VIDEO_CAPTURE =============================

import cv2
import numpy as np

def nothing(x):
    pass

def Obj_Tracking():
    Camera_ID = 0
    cap = cv2.VideoCapture(Camera_ID)
    cv2.namedWindow("Tracking")
    cv2.createTrackbar("LH", "Tracking", 0, 179, nothing)
    cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("UH", "Tracking", 0, 179, nothing)
    cv2.createTrackbar("US", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("UV", "Tracking", 0, 255, nothing)
    while True:
        _, frame = cap.read()
        if cv2.waitKey(10) == ord("q"):
            break
        HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        L_H = cv2.getTrackbarPos("LH", "Tracking")
        L_S = cv2.getTrackbarPos("LS", "Tracking")
        L_V = cv2.getTrackbarPos("LV", "Tracking")
        U_H = cv2.getTrackbarPos("UH", "Tracking")
        U_S = cv2.getTrackbarPos("US", "Tracking")
        U_V = cv2.getTrackbarPos("UV", "Tracking")
        Lower_Color = np.array([L_H, L_S, L_V])
        Upper_Color = np.array([U_H, U_S, U_V])
        mask = cv2.inRange(HSV, Lower_Color, Upper_Color)
        result = cv2.bitwise_and(frame, frame, mask = mask)
        cv2.imshow("Origin_Image", frame)
        cv2.imshow("Masked_Image", mask)
        cv2.imshow("Result_Image", result)
    cap.release()
    cv2.destroyAllWindows()

def main():
    Obj_Tracking()

if __name__ == "__main__":
    main()

