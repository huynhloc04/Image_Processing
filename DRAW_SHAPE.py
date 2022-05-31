
import cv2
import numpy as np

def Read_Image():
    img = cv2.imread("Bong_Bay.jpg")
    
    #   Create a Black_Image by using "numpy" with np.zeros() 
    #img_Bl = np.zeros([512,512,3])    #   Tạo 1 ảnh Black_Image với height,width,channel là [512,512,3]

    #   Create a White_Image with numpy by using np.ones()
    #img_Bl = np.ones([512,512,3]) 

    #   Vẽ Line bình thường
    img_l = cv2.line(img, (0,0), (508,420), (0,255,0), 10)     # Màu BGR của Line: (BLUE, GREEN, RED), 10: độ dày của Line
    #   Có thể chọn Màu của line thông qua tra Gg: RGB color piker

    #   Vẽ Line là một mũi tên
    img_n = cv2.arrowedLine(img, (0,0), (320,255), (0,255,0), 2)

    #   Vẽ hình chữ nhật (RECTANGLE)  ========== Syntax: cv2.rectangle(img, (top_left_point), (lower_right_point), color, thickness) =========
    img_rt = cv2.rectangle(img, (50,50), (250, 250), (0,255,0), -1)  # (50,50): điểm trên cùng bên trái của HCN, (250,250): điểm dưới cùng 
                                            #  bên phải của HCN, nếu thay độ dày của Line (2 -> -1), ta sẽ có một HCN được lấp đầy một màu

    #   Vẽ CIRCLE    =============Syntax: cv2.circle(img, centre, radius, color, thickness) ================
    img_cc = cv2.circle(img, (254,210), 100, (255,0,0), -1)

    #   Viết VĂN BẢN:  ======= Syntax: cv2.putText(img, "your_Text", "Text's start_position", font_chữ, Size_chữ, color, thickness, line_Style) =======
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    img_T = cv2.putText(img, "OpenCV", (10,210), font, 1, (0,0,0), 2, cv2.LINE_4)

    #   Vẽ đa giác (TAM GIÁC):
    Coordinate = np.array([0, 0], [50,0], [25, 75]) #   Nhập số tọa độ ứng vs số cạnh của đa giác cần vẽ
    triangle = cv2.polylines(img, [Coordinate], True, (0,255,0), -1)    #   Tham số True: là 1 đa giác khép kín

    cv2.imshow("Bong_Bay", img_T)
    cv2.waitKey()
    #   Hàm trả về số pixel của hàng và số pixel của chiều cột => (số pixel hàng (c.rộng), số pixel cột (c.dài), channel) VD; (420,580,3)
    print(img.shape) #  Cách 2: https://note.nkmk.me/en/python-opencv-pillow-image-size/
    h, w, _ = img.shape     #   Để biết width, height là cái nào thì xem ảnh width_height.jpg
    print(w)    #   Number of row
    print(h)    #   Number of column
    cv2.destroyAllWindows()

Read_Image()