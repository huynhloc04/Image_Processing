
# import cv2
# import numpy as np
# prevX, prevY = 1, 1

# def MouseCallback(event, x, y, flags, param):
#     #   Khai báo biến toàn cục
#     global prevX, prevY
#     print(x,", ",y)
#     if event == cv2.EVENT_LBUTTONDOWN:  #   Gọi phương thức khi click chuột trái
#         #  Vẽ ra một chấm tròn
#         cv2.circle(img, (x,y), 3, (0,255,0), -1)
#         text = f"[{x}, {y}]"
#         font = cv2.FONT_HERSHEY_COMPLEX_SMALL
#         cv2.putText(img, text, (x+10,y-10), font, 0.55, (0,255,0), 1, cv2.LINE_8)
#         if prevX == 1 and prevY == 1:
#             prevX, prevY = x, y
#         else:
#             cv2.line(img, (prevX,prevY), (x,y), (0,0,255), 2)
#             prevX, prevY = 1, 1
#         cv2.imshow("Image", img)
#     if event == cv2.EVENT_RBUTTONDOWN:
#         blue = img[y,x,0]
#         green = img[y,x,1]
#         red = img[y,x,2]
#         strBGR = f"[{blue}, {green}, {red}]"
#         font = cv2.FONT_HERSHEY_COMPLEX_SMALL
#         cv2.circle(img, (x,y), 3, (0,255,255), -1)
#         cv2.putText(img, strBGR, (x+10,y-10), font, 0.55, (0,255 ,255), 1, cv2.LINE_8)
#         cv2.imshow("Image", img)
#     #if event == cv2.EVENT_MBUTTONDOWN:
#     print("===================", type(flags))


# img = np.zeros((512,512,3), np.uint8)
# #img = cv2.imread("Touno_V4.jpg")
# cv2.imshow("Image", img)
# cv2.setMouseCallback("Image", MouseCallback)
# cv2.waitKey()
# cv2.destroyAllWindows()


import cv2
import numpy as np
def Mouse_Back(event, x, y, flags, params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 10, (0,0,255), -1)
        print(flags)
        # text = f"[{x},{y}]"
        # font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        # cv2.putText(img, text, (x,y), font, 0.55, (255,0,0), 1, cv2.LINE_AA)
        # cv2.imshow("Image", img)
        # #   Tạo 1 cửa sổ mới để fill 1 màu tại điểm click của cửa sổ trước đó
        # blue = img[y,x,0]
        # green = img[y,x,1]
        # red = img[y,x,2]
        # One_Color = np.zeros((512,512,3), np.uint8)
        # #     Lệnh One_Color[:] là để toàn bộ cái ảnh đều fill bằng màu blue, green, red 
        # #  (nói cách khác là toàn bộ các ptu trong List ảnh đều có giá trị của Màu RGB tại điểm click chuột phải)
        # One_Color[:] = [blue, green, red]
        cv2.imshow("Image", img)

    #   Click chuột trái để nối các điểm LIÊN TIẾP bằng line
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     cv2.circle(img, (x,y), 3, (0,255,0), -1)
    #     text = f"[{x},{y}]"     #   Tạo text với định dạng [120,250]
    #     font = cv2.FONT_HERSHEY_COMPLEX_SMALL   #   Chọn font chữ
    #     cv2.putText(img, text, (x+10,y-10), font, 0.55, (255,0,0), 1, cv2.LINE_AA)
    #     point.append((x,y)) #Thêm từng điểm vào trong List point
    #     #   Nếu chiều dài của List < 2 thì chỉ show cái điểm đó ra, còn nếu List từ 2 đỉm trờ lên thì nối lại bằng Line
    #     if len(point) >= 2:
    #         #   Điểm đầu phải là point[-1] điểm 2 là point[-2] vì các điểm nối đuôi nhau, điểm đầu của thk này sẽ là điểm cuối của thk trước đó 
    #         #   Cái này hay vl, lưu vào não nhanh
    #         cv2.line(img, point[-1], point[-2], (0,0,255), 2)
    #     cv2.imshow("Image", img)

#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread("Factory.jpg")
cv2.imshow("Image", img)
#   Tạo ra một cái List để thêm các điểm vào
#point = []
cv2.setMouseCallback("Image", Mouse_Back)
#     Tại sao trong hàm setMouseCallback, hàm "Mouse_Back" không truyền các tham số vào?
#     Bởi vì hàm tại tham số thứ 2 của hàm setMouseCallback là (Mouse_Back), khi click chuột thì lần lượt các giá trị 
#  event; tọa độ x,y; flags; param được gán vào hàm Mouse_Back, khi gọi hàm Mouse_Back, các thông số này lần lượt gán 
#  có thứ tự tại các vị trí của hàm def Mouse_Back(event, x, y, flags, param): => Từ đó, có thể làm việc với các thông số này trong hàm
cv2.waitKey()
cv2.destroyAllWindows()


