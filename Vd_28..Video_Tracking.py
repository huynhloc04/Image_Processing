# # #   Step 1: Find out the difference between the frame1 and the frame2
# # #   Step 2: Use GaussianBlur to eleminate noises
# # #   Step 3: Use threshold
# # #   Step 4: Use Dilate for eleminating district small week 
# # #   Step 5: Finding contours from the clean threshold
# # #   Step 6: Draw the contour
# # #   Step 7: 


#   ========================= https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/ ================================


# import cv2
# import numpy as np
# import datetime as dt
# cap = cv2.VideoCapture("Motion_Vd.mp4")
# _, frame1 = cap.read()
# _, frame2 = cap.read()
# while(cap.isOpened()):
#     if cv2.waitKey(10) == ord("q"):
#         break
#     #   Find out the absolute difference between the frame1 and the frame2
#     diff = cv2.absdiff(frame1, frame2)
#     # cv2.imshow("DIFF", diff)
#     gray_img = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
#     # #   Use gaussianBlur to eleminate the noise of diff
#     # blur = cv2.GaussianBlur(gray_img, (3,3), 0)
#     #   Make threshold
#     _, Thresh = cv2.threshold(gray_img, 10, 255, cv2.THRESH_BINARY)
#     cv2.imshow("Threshold", Thresh)
#     #   Use DILATE
#     kernal = np.ones((3,3), np.uint8)
#     Dilation = cv2.dilate(Thresh, kernal, iterations = 1)
#     #Dilation = cv2.morphologyEx(Thresh, cv2.MORPH_CLOSE, kernal)
#     cv2.imshow("Dilation", Dilation)
#     #   Find contour
#     contours, _ = cv2.findContours(Dilation, cv2.RETR_TREE, cv2. CHAIN_APPROX_SIMPLE)
#     #  =>=>=> Những bước trên đây chỉ để giúp tìm ra Contour 1 cách dễ dàng bằng cách loại bỏ đi những noise, ảnh mờ để tìm ra Contour

#     #   Draw contour
#     #cv2.drawContours(frame1, contours, -1, (0,255,0), 2)

#     # Draw rectangleq
#     for i in range(len(contours)):
#         (x, y, width, height) = cv2.boundingRect(contours[i])
#         #   Hàm cv2.boundingRect() trả về 1 cách ước lượng của 1 cái rectang để vẽ xung quanh cái contour vừa tìm đc
#         if cv2.contourArea(contours[i]) < 2000:   #     Nếu diện tích của cái Contour nhỏ hơn 700, thì ta sẽ ko vẽ rectangle, => cách để lọc, loại bỏ đi những 
#             continue                #   cái contour ko phải là người
#         #   Tiến hành vẽ Rectangle thôi nào
#         cv2.rectangle(frame1, (x,y), (x+width, y+height), (0,255,0), 2)
#         font = cv2.FONT_HERSHEY_COMPLEX_SMALL
#         cv2.putText(frame1, f"No.{i+1}", (x+5, y+5), font, 0.5, (0,0,255), 1, cv2.LINE_AA)

#     #   Put DATE_TIME Text on Video
#     datetime = str(dt.datetime.now())
#     font = cv2.FONT_HERSHEY_COMPLEX_SMALL
#     frame_n = cv2.putText(frame1, datetime, (15,25), font, 1, (0,0,255), 2, cv2.LINE_AA)

#     cv2.imshow("FEED", frame_n)
#     frame1 = frame2
#     _, frame2 = cap.read()                       
            
# cap.release()
# cv2.destroyAllWindows()



import cv2
import numpy as np
cap = cv2.VideoCapture("Motion_Vd.mp4")
_, frame_1 = cap.read()
_, frame_2 = cap.read()
while(cap.isOpened()):
    diff = cv2.absdiff(frame_1, frame_2)
    img_gr = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Diff_Image", img_gr)
    _, Thresh = cv2.threshold(img_gr, 10, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(Thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 400:
            (x, y, width, height) = cv2.boundingRect(cnt)
            cv2.rectangle(frame_1, (x, y), (x+width, y+height), (0,255,0), 2)
            cv2.imshow("Person_Tracking", frame_1)
    frame_1 = frame_2
    _, frame_2 = cap.read()
    if cv2.waitKey(10) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()