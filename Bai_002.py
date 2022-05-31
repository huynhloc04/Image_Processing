#     Đọc ảnh từ 1 File video và hiểm thị lên màn hình. Nếu người dùng nhấn phím A thì quay màn hình ngược chiều KDH 90 độ
#  còn nếu ấn phím D thì quay cùng chiều KDH 90 độ

import cv2 as cv
import imutils as im

def Camera_Read():
    Camera_ID = 0
    cap = cv.VideoCapture(Camera_ID)
    rotate = 0
    while True:
        ret, frame = cap.read()
        if ret:
            if rotate != 0:
                frame = im.rotate(frame, rotate)
            cv.imshow("Rotate_Picture", frame)
        key = cv.waitKey(10)
        if key == ord("a"):
            rotate = 90
        elif key == ord("d"):
            rotate = -90
        elif key == ord("q"):
            break
        else:
            rotate = 0
    cap.release
    cv.destroyAllWindows()

def main():
    Camera_Read()

if __name__ == "__main__":
    main()