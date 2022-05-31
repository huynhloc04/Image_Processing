import cv2
import numpy as np 

def nothing(x):
    pass

img = np.zeros((512,700,3), np.uint8)      #    img = np.zeros((no. ofrows, no.columns, channel), np.uint8)
# img_st = cv2.imread("Kawasaki.png")
# img = cv2.resize(img_st, (512,700))
cv2.namedWindow("Image")
cv2.createTrackbar("B", "Image", 0, 255, nothing)
cv2.createTrackbar("G", "Image", 0, 255, nothing)
cv2.createTrackbar("R", "Image", 0, 255, nothing)
#     Tại sao trong hàm createTrackbar, hàm "nothing" không truyền các tham số vào?  => xem giải thích tương tự tại file_code: HANDLE_MOUSE.py
#     Vì khi gọi hàm createTrackbar, một khi thay đổi trên thanh Trackbar thì giá trị thay đổi (x) sẽ được gán vào cho tham số thứ 5 là hàm nothing
#   Từ đó, ta có thể gọi hàm nothing với đối số x để hiện thị ra màn hình. Bản chất của tham số "nothing" là lấy giá trị thay đổi của thanh Trackbar 
#   khi ta thay đổi và gọi hàm nothing để hiển thị giá trị thay đổi đó ra. Mặt khác, nếu ta truyền tham số vào hàm "nothing" thì vô hình ta đã làm  
#   thay đổi giá trị đó

#   Create a switch
switch = "0: OFF \n 1: ON"
cv2.createTrackbar(switch, "Image", 0, 1, nothing)
while True:
    if cv2.waitKey(10) == ord("q"):
        break
    #   Get the current value of the one by one of Trackbars
    B = cv2.getTrackbarPos("B", "Image")
    G = cv2.getTrackbarPos("G", "Image")
    R = cv2.getTrackbarPos("R", "Image")
    S = cv2.getTrackbarPos(switch, "Image")
    if S == 0:
        img[:] = 0
    #   Set these value to the image
    else:
        img[:] = [B,G,R]
    cv2.imshow("Image", img)
cv2.destroyAllWindows()




#      SỬ DỤNG Trackbar ĐỂ CHUYỂN ĐỔI ẢNH MÀU SANG ẢNH XÁM

import cv2
import numpy as np 

def nothing(x):
    pass

cv2.namedWindow("Image")
cv2.createTrackbar("Black_White", "Image", 0, 255, nothing)
#   Create a switch
switch = "0: COLOR \n 1: BLACK_WHITE"
cv2.createTrackbar(switch, "Image", 0, 1, nothing)
while True:
    img_st = cv2.imread("Kawasaki.png")
    img = cv2.resize(img_st, (1200,700))     #   cv2.resize(img, (width,height))
    if cv2.waitKey(10) == ord("q"):
        break
    #   Get the current value of the one by one of Trackbars
    S = cv2.getTrackbarPos(switch, "Image")
    Pos = cv2.getTrackbarPos("Black_White", "Image")
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(img, str(Pos), (250, 250), font, 2, (0, 255, 0), 1, cv2.LINE_8)
    if S == 0:
        pass
    #   Set these value to the image
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image", img)

cv2.destroyAllWindows()




