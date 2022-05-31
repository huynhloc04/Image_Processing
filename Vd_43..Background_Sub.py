#       Count object is moving

#   ============================= Background_Subtractor Using Difference ============================
import cv2
import numpy as np 
cap = cv2.VideoCapture("highway.mp4")
_, frame_1 = cap.read()
_, frame_2 = cap.read()
while(cap.isOpened()):
    # ret, frame = cap.read()
    # if ret:
    #     cv2.imshow("Image", frame)
    diff = cv2.absdiff(frame_1, frame_2)
    diff_gr = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    Gblur = cv2.GaussianBlur(diff_gr, (3,3), 0)
    _, Threshold = cv2.threshold(Gblur, 20, 255, cv2.THRESH_BINARY)
    cv2.imshow("Diff_Image", Threshold)
    frame_1 = frame_2
    _, frame_2 = cap.read()
    if cv2.waitKey(10) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()




