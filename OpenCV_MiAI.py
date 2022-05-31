
import cv2
import imutils as im    #   Import thư viện này để xoay ảnh dễ hơn

#   Đọc ảnh từ Camera
def Camera_Read():
    Camera_ID = 0
    #   Mở Camera
    cap = cv2.VideoCapture(Camera_ID)
    while True:
        ret, frame = cap.read()
        cv2.imshow("Cam", frame)
        if cv2.waitKey(10) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

#   Đọc ảnh từ file
def File_Picture():
    img = cv2.imread("Yamaha_R1.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Anh", img)
    cv2.waitKey()
    cv2.imwrite("Yamaha_R1-Black_White.jpg", img)
    destroyAllWindows()

#   Chuyển đổi sang hệ màu RGB
def Convert_RGB():
    img = cv2.imread("Yamaha_R1.jpg")
    img_2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Anh chuyen", img_2)
    cv2.waitKey()
    cv2.destroyAllWindows()

#   Thay đổi kích thước ảnh
def Resize():
    img = cv2.imread("Yamaha_R1.jpg")
    img_2 = cv2.resize(img, (400,300))
    #   cach_2: img_2 = cv2.resize(img, dsize = None, fx = 2, fy = 2)
    cv2.imshow("Resize", img_2)
    cv2.waitKey()
    cv2.destroyAllWindows()

#   Xoay ảnh sử dụng thư viện "imutils"
# def Rotate_Picture():
#     img = cv2.imread("Yamaha_R1.jpg")
#     img_rt = im.rotate(img, 270)
#     cv2.imshow("Xoay anh", img_rt)
#     cv2.waitKey()
#     cv2.destroyAllWindows()

#   Xoay ảnh sử dụng thư viện "imutils"
def Rotate_Picture():
    img = cv2.imread("Yamaha_R1.jpg")
    img_2 = im.rotate(img, 45)
    img_3 = cv2.resize(img_2, dsize = None, fx = 0.5, fy = 0.5)
    cv2.imshow("Xoay anh", img_3)
    cv2.waitKey()
    cv2.destroyAllWindows()

#   Đưa ảnh về ảnh nhị phân
def Anh_Nhi_Phan():
    img_st = cv2.imread("DUCATI_V4R.png", cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img_st, dsize = None, fx = 0.5, fy = 0.5)
    cv2.imshow("Black_White_Picture", img)
    cv2.waitKey()
    #   Những điểm ảnh nào có giá trị màu lớn hơn 70 thì gán cho nó là 255 luôn -> thành điểm ảnh TRẮNG
    ret, binary_pc = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binary_picture", binary_pc)
    cv2.waitKey()
    #   Lưu ảnh  => "cv2.imwite"
    cv2.imwrite("Binary_picture.jpg", binary_pc)
    cv2.destroyAllWindows()

#   Đưa ảnh xám về ảnh nhị phân sử dụng Adaptive_Threshold
def Threshold_Binary():
    img_st = cv2.imread("Threshold_Image.jpg", cv2.IMREAD_GRAYSCALE)
    #   Thu nhỏ ảnh thành một nửa
    #img_st = cv2.resize(img_n, dsize = None, fx = 1, fy = 1)
    cv2.imshow("Binary_Image", img_st)
    cv2.waitKey()
    img_st = cv2.medianBlur(img_st, 5)
    img = cv2.adaptiveThreshold(img_st, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imshow("Threshold_Binary_Image", img)
    cv2.waitKey()
    cv2.imwrite("Threshold_Binary_Image.jpg", img)
    cv2.destroyAllWindows()

#   Hàm tìm viền ảnh
def Vien_Anh():
    img_1 = cv2.imread("Threshold_Image.jpg", 0)   # Tham số 0 để chuyển ảnh màu về ảnh xám
    #   Thu nhỏ anh xuống 1/2
    #img_1 = cv2.resize(img, dsize = None, fx = 0.5, fy = 0.5)
    cv2.imshow("Sodoku", img_1)
    cv2.waitKey()
    #   Viền ảnh
    img_2 = cv2.Canny(img_1, threshold1 = 100, threshold2 = 200)
    #   Làm mờ -> Giảm nhiễu
    #img_n = cv2.GaussianBlur(img_2,(3,3),0)
    cv2.imshow("Vien_Anh", img_2)
    cv2.waitKey()
    cv2.destroyAllWindows()

#   Hàm làm mờ ảnh, giảm nhiễu
def Giam_Nhieu():
    #   Ảnh đầu vào không cần là ảnh xám, ảnh màu là OK
    img = cv2.imread("Threshold_Image.jpg")
    cv2.imshow("Sodoku", img)
    cv2.waitKey()
    img_1 = cv2.GaussianBlur(img,(3,3),0)
    cv2.imshow("Anh_Giam_Nhieu", img_1)
    cv2.waitKey()
    cv2.destroyAllWindows()

#   Tìm đường viền của object trong ảnh
def Search_Contours():
    pass


def main():
    #Camera_Read()
    #File_Picture()
    #Convert_RGB()
    #Resize()
    #Rotate_Picture()
    Anh_Nhi_Phan()
    #Threshold_Binary()
    #Vien_Anh()
    #Giam_Nhieu()

if __name__ == "__main__":
    main()

