
#   Tutorial: https://learnopencv.com/opencv-threshold-python-cpp/
#            Otsu's: https://learnopencv.com/otsu-thresholding-with-opencv/
#               https://www.youtube.com/watch?v=Ofi1Fn18YLc&t=186s


# #   =============================  SIMPLE THRESHOLD ===========================

# import cv2
# from matplotlib import pyplot as plt
# img_st = cv2.imread("Gradient.jpg")
# img = cv2.cvtColor(img_st, cv2.COLOR_BGR2RGB)  #    ==> Chuyển đổi sang hệ RGB để show đúng màu khi sd phương pháp Matplotlib 
# #img = cv2.resize(img_st, (400,250))

# #   Tạo ảnh nhị phân từ "Gradient", những pixel ảnh có giá trị > 127 chuyển sang WHITE_Color, ngược lại chuyển sang Black_Color
# _, Thresh_1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# #   Tạo ảnh nhị phân chuyển ngược của Thresh_1 => cv2.THRESH_BINARY_INV
# _, Thresh_2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# #   Tạo ảnh giữ nguyên giá trị của các điểm ảnh < threshold, những giá trị lớn hơn threshold -> gán cho chúng giá trị = const = threshlod
# _, Thresh_3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

# #   Tạo ảnh giữ nguyên giá trị của các điểm ảnh > threshold, những giá trị nhỏ hơn threshold -> gán cho chúng giá trị = ZERO (Black_Color)
# _, Thresh_4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

# #   Tạo ảnh đảo ngược trái phải như phương thức BINARY_INV
# _, Thresh_5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# # cv2.imshow("Origin_Image", img)
# # cv2.imshow("Thresh_1", Thresh_1)
# # cv2.imshow("Thresh_2", Thresh_2)
# # cv2.imshow("Thresh_3", Thresh_3)
# # cv2.imshow("Thresh_4", Thresh_4)
# # cv2.imshow("Thresh_5", Thresh_5)


# #   ===================== Thay vì show các ảnh nhiều lần như trên, ta sd thư viện MATPLOTLIB =====================
# titles = ["Origin_Image", "BINARY_IMG", "BINARY_INV_IMG", "TRUNC_IMG", "TOZERO_IMG", "TOZERO_IVN_IMG"]
# images = [img, Thresh_1, Thresh_2, Thresh_3, Thresh_4, Thresh_5]
# for i in range(6):
#     plt.subplot(2, 3, i+1), plt.imshow(images[i])
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()  #   ==> Không cần waitKey

# # cv2.waitKey()
# # cv2.destroyAllWindows()




#   ============================ ADAPTIVE THRESHOLD ============================
import cv2
img = cv2.imread("Sodoku.jpg", 0)   #  Có thêm argument "0" là vì để chuyển ảnh sang ảnh XÁM mới sử dụng đc các phương pháp threshlod
cv2.imshow("SODOKU_IMAGE", img)

#   Simple Threshold method
_, Thresh_1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("SODOKU_THRESH", Thresh_1)

#   Adaptive_Threshold method       => Muốn sử dụng phương pháp này thì phải CHUYỂN về ẢNH XÁM
Adt_Thresh_MEAN_C = cv2.adaptiveThreshold(img, 200, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("SODOKU_ADAPTIVE_MEAN_C", Adt_Thresh_MEAN_C)
#       Từng pixel trong ảnh sẽ được duyệt qua lần lượt bằng 1 "BLOCKSIZE" để tìm ra giá trị ngưỡng của pixel ảnh đó. Có 2 cách để tìm ra
#   giá trị ngưỡng(Threshold), ===== CÁCH 1: cv2.ADAPTIVE_THRESH_MEAN_C =====. CÁCH 2: cv2.ADAPTIVE_THRESH_GAUSSIAN_C. Nếu giá trị của 
#   pixel đó lớn hơn giá trị ngưỡng thì giá trị pixel đó sẽ đc gán bằng giá trị của argument thứ 2 trong hàm (đó là giá trị MAX VALUE. 
#   VD: 255 (Cũng tùy thuộc vào argument thresholdType, có 4 thresholdType cơ bản trình bày ở trên phần ======= SIMPLE THRESHOLD =======)).
#   Tham số 5: 11 là kích thước của 1 BLOCKSIZE, là 1 ma trận vuông LẻxLẻ và lớn hơn 1
#   --------THAM KHẢO WEB--------:  https://www.tutorialspoint.com/opencv/opencv_adaptive_threshold.htm
 
Adt_Thresh_GAUSSIAN = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("SODOKU_ADAPTIVE_GAUSIAN", Adt_Thresh_GAUSSIAN)
cv2.waitKey()
cv2.destroyAllWindows()
