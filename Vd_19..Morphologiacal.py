# import cv2 as cv2
# from matplotlib import pyplot as plt
# img = cv2.imread("Factory.jpg")
# cv2.imshow("Image", img)
# img_2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    #   ==> Chuyển đổi sang hệ RGB để show đúng màu khi sd phương pháp Matplotlib, hoặc thêm "gray"
#   làm argument thứ 2 tron hàm plt.imshow() ở dòng 33

# #   Ẩn hai trục tọa độ
# plt.xticks([]), plt.yticks([])

# #   Hiển thị nhiều cửa sổ (nhiều ảnh cùng 1 lúc)  ==> Xem Vd_15..Threshold.py
# for i in range(6):
#     print(i)
# #   Xuất ảnh bằng MATPLOTLIB ==> Khỏi sd waitKey
# plt.imshow(img_2)
# plt.show()

# cv2.waitKey()
# cv2.destroyAllWindows()



#   =================================== MORPHOLOGICAL TRANSFORMATION ====================================

#   Links: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html
#          http://datahacker.rs/006-morphological-transformations-with-opencv-in-python/

import cv2 as cv2
from matplotlib import pyplot as plt
import numpy as np
    #   Morphological transformation on the Binary image ==> Create a MASK
img = cv2.imread("Color_Ball.jpg", 0)
_, mask = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Origin_Mask", mask)

#       CÁCH 1: In some case, phần trắng của MASK sẽ có lốm đốm những chấm đen, ta sd phương thức "DILATE" để xóa đi những chấm đen đó
#    bằng cách tạo ra một cái kernel màu trắng(1 cái mtr toàn số 1), sau đó đè lên nhứng chấm đen đó, kích thước của kernel càng lớn, 
#    càng che được chấm đen càng lớn. Nhưng cũng đừng quá lạm dụng việc tăng kích thước của KERNEL, nếu kích thước quá lớn nó kernel sẽ ngập ra
#    và làm biến dạng ảnh(phần trắng của MASk lan lớn ra)
kernal = np.zeros((3,3), np.uint8)
dilation = cv2.dilate(mask, kernal) 
cv2.imshow("Image_Kernal", dilation)
dil = cv2.dilate(mask, None) #  "None" equivalent to Kernal=3
print("===============\n", dil.max())
cv2.imshow("Image_None", dil)
cv2.waitKey()
cv2.destroyAllWindows()
#       CÁCH 2: Tham số thứ 3 sử dụng trong hàm dilate là "iterations = k", nó lặp lại k lần dilate, tức là nó sẽ tìm điểm đen và lấp lại bằng những khoảng
#    trắng k lần    ==> Cách nào cũng làm kích thước của vùng trắng lớn hơn  ==> Sd phương thức mới: ERODE

#dilation = cv2.dilate(mask, kernal)
dilation = cv2.dilate(mask, kernal, iterations = 2) #   cv2.dilate có xu hướng làm TĂNG KÍCH THƯỚC phần trắng
#   Sử dụng ERODE: Kernel sẽ duyệt lần lượt tất cả các Pi(mtr các pixel bằng kích thước của kernel) trong ảnh, nếu Pi là màu trắng thì sẽ 
#   chuyển thành màu trắng, còn nếu có 1 cái pixel nào trong Pi là màu đen, thì Pi đó(các pixel nằm dưới kernel) sẽ thành màu đen hết
#   ==> cách nay tui thấy ít hiệu quả hơn
erosion = cv2.erode(mask, kernal, iterations = 1) #   cv2.erode có xu hướng làm GIẢM KÍCH THƯỚC phần trắng

#       CÁCH 3: Sử dụng Opening_Morphological ==> Kết hợp cv2.dilate và cv2.erode. Sử dụng cv2.erode trước, cv2.dilate sau
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

#       CÁCH 4: Sử dụng Closing_Morphological ==> Kết hợp cv2.dilate và cv2.erode. Sử dụng cv2.dilate trước, cv2.erode sau
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

titles = ["Origin Image", "MASK", "DILATION", "EROSION", "OPENING", "CLOSING"]
Images = [img, mask, dilation, erosion, opening, closing]
for i in range(6):
    plt.subplot(2, 3, i+1)  #     Syntax: plt.subplot(row, cols, index of image) Chuẩn bị một khung hình để show các ảnh thành row hàng và cols cột, 
                            #   i+1 là chỉ số các ảnh trong từng vòng lặp
    plt.imshow(Images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()