
#   Đọc ảnh từ camera và chyển sang màu xám, hiển thị trên màn hình

import cv2 as cv
import imutils as im

def Camera_Read():
    Camera_ID = 0
    #   Mở Camera
    cap = cv.VideoCapture(Camera_ID)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter("Video_Capture.mp4", fourcc, 20, (640,480))
        # "Video_Capture.mp4" :  Tên file để lưu Video_Capture
        # 20 :  Lưu 20 khung hình trên 1 giây
        # (640,480) :  Kích thước của khung hình, dài 640 pixels, rộng 480 pixels
    while(cap.isOpened()):      #     Phương thức cap.isOpened() sẽ trả về kiểu True hoặc False, nếu Camera_Id (index của Camera hoặc đường dẫn) 
                                #   truyên vào đúng thì sẽ tiếp tục ct, nếu sai thì thoát ct
        ret, frame = cap.read()
        if ret:
            # print(cap.get(cv.CAP_PROP_FRAME_WIDTH))   trả về chiều rộng khung hình
            # print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))   trả về chiều dài khung hình
            out.write(frame)
            #img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imshow("Cam", frame)
        if cv.waitKey(10) == ord("q"):
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()

def main():
    Camera_Read()

if __name__ == "__main__":
    main()
