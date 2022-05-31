
import cv2
import datetime as dt
cap = cv2.VideoCapture(0)
cap.set(3,1280)     
cap.set(4,720)    
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        #text = "Width: " + str(cap.get(3)) + "  " + "Height: " + str(cap.get(4))
        datetime = str(dt.datetime.now())
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        frame = cv2.putText(frame, datetime, (20,20), font, 1, (0,0,255), 2, cv2.LINE_4)
        #   RECTANGLE
        frame = cv2.rectangle(frame, (540,260), (740, 420), (0,255,0), 2)
        cv2.imshow("Picture", frame)
    if cv2.waitKey(10) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
 