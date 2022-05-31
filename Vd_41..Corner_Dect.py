
#   File ảnh sử dụng trong bài: Flag.jpg, House_Corner.jpg, Corner_Det.jpg

#   =========================================== Harris Corner Detector ========================================

#       LINK:       1. *********** https://stackoverflow.com/questions/7263621/how-to-find-corners-on-a-image-using-opencv ************
#                   2. Ứng dụng cornerHarris: https://viblo.asia/p/ung-dung-thuat-toan-harris-corner-detector-trong-bai-toan-noi-anh-phan-i-ByEZkyME5Q0
#                   3. https://docs.opencv.org/3.4/dc/d0d/tutorial_py_features_harris.html
#                   4. Stackoverflow: https://stackoverflow.com/questions/54720646/what-does-ksize-and-k-mean-in-cornerharris
#                   5. https://viblo.asia/p/corner-detection-voi-opencv-eW65Gv6YlDO


#     Harris Corner detector is used to extract (trích xuất) corners from GRAYSCALE images. 
#     What is CORNER: Corners are the region in the image with large VARIATION(Sự thay đổi) in intensity(cường độ) in all direction. 
#   Or a corner can be interpreted(đc giải thích) as the junction(chỗ nối) of two edges (where an edge is a sudden change in image brightness).

#    => Step 1. Detect the "window". The window is the region in rectangle (small box) cover the coners with the change or large variation 
#  in the intensity when u move in the X-direction or Y-direction

#    => Step 2. With each such window, we compute (tính toán) a R-score. R-score will give us the estimate or an idea about where this corner is located
#      ====================     R = det(M) - k*(trace(M))^2    ===================      Xem file ảnh M_Matrix.jpg
#                                  - det(M)   : Hạng của m.trận = lamda1*lamda2
#                                  - trace(M) : Vết của m.trận  = lamda1 + lamda2
#                                  - k in [0.04, 0.06]
#                                  - lamda    : trị riêng của vector
#                                  - M        : Ma trận vuông cấp 2x2

#    => Step 3. We apply the Threshold (ngưỡng) for this R-score then the important corners are selected and marked

#       ============================= SYNTAX:  cv2.cornerHarris(img, window, ksize, k_par) =============================
#                      - img: ảnh muốn xác định góc
#                      - window: 1 cái cửa sổ để tạo m.trận M và tính toán g.trị R
#                      - ksize: kích thước của kernel sử dụng cho quá trình Sobel đc th.hiện ngầm định trong cornerHarris
#                      - k_par: hệ số tự do trong phương trình xác định R, thông thường lấy trong đoạn [0.04 : 0.06]. k_par càng nhỏ thì xác định đc nhiều góc hơn
#                           thay vào đó, các góc nhiễu(ko phải góc) sẽ bị detect nhầm. Còn nếu k_par lớn thì các góc đúng có thể bị detect sót, nhưng các góc nhiễu thì lại ít đi

#                   ============================= Cách thức hoạt động =============================
#       Giải thuật sẽ sử dụng ảnh xám mà ta đã chuyển đổi , sd phương thức Sobel để tìm các cạnh trong ảnh, sau đó sẽ dùng 1 Window để lướt dọc theo
#    cạnh của các Object trong hình, trong quá trình quét, tại mỗi vị trí của Window, giải thuật sẽ tính toán giá trị R và trả về dưới dạng 1 m.trận 
#    nếu giá trị R tại vị trí nào mà lớn hơn Threshold thì sẽ là vị trí góc của ảnh. Sau đó, ta sd cv2.dilate() để làm rõ(to) hơn những nốt trắng(đại diện cho các góc đã detect đc)

# import cv2
# import numpy as  np 
# img = cv2.imread("flag.png")
# img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_gr = np.float32(img_gr)
# dst = cv2.cornerHarris(img_gr, 4, 3, 0.04)
# cv2.imshow("First_dst", dst) 
# #   Dilate (v) = Expand: Mở rộng, lan rộng
# #   Erode  (v): Thu hẹp, ăn mòn
# #   Sử dụng phương thức cv2.dilate() để làm rõ các nốt trắng đã đc xác định bởi hàm cornerHarris() bằng cách làm to hơn kích thước của các nốt trắng (màu trắng)
# # dst = cv2.dilate(dst, None)
# #   Những giá trị R nào lớn hơn ngưỡng Threshold đã chỉ định, thì được tô màu và hiện ra màn hình. Giá trị R thỏa là những nốt trắng đã detect được sau khi thực hiện hàm cv2.cornerHarris()
# # Giá trị R cụ thể là phần tử trong m.trận ảnh, phàn tử nào cố giá trị lớn hơn Threshold thì đc tô màu
# img[dst > 0.01*dst.max()] = [0, 255, 0]
# cv2.imwrite("Harris.png", img)
# cv2.imshow("Image_2", img)
# cv2.waitKey()
# cv2.destroyAllWindows()





#   ================================= Shi-Tomasi  cv2.goodFeaturesToTrack =================================

#       LINK: https://www.youtube.com/watch?v=I7lCpTOfxF4
#             https://docs.opencv.org/master/d4/d8c/tutorial_py_shi_tomasi.html
#             Cụ thể nhất: https://docs.opencv.org/3.4/dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541
#             https://viblo.asia/p/corner-detection-voi-opencv-eW65Gv6YlDO

#   Theory: In cornerHarris, R is calculated: R = det(M) - k*(trace(M))^2
#           but in Shi Tomasi, R is propsoed: R = min(lamda_1, lamda_2)


import cv2
import numpy as  np 
img = cv2.imread("flag.png")

#   Create a mask
# mask = np.zeros_like(img)
# cv2.rectangle(mask, (200,100), (500, 350), (255,255,255), -1)
# cv2.imshow("Mask", mask)
kernel = np.zeros((5, 5), np.uint8)
img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(img_gr, 800, 0.01, 0.3)    # Hàm sẽ trả về tọa độ của các điểm đã detect đc dưới dạng 1 m.trận 3 chiều
#   - 1000: Maximum number of corners to return. If there are more corners than are found, the strongest of them is returned. 
#  MaxCorners <= 0 implies that no limit on the maximum is set and all detected corners are returned.
#   - 0.003:  Parameter characterizing the minimal accepted quality of image corners.The corners with the quality measure less than the product are rejected.
#   - Minimum possible Euclidean_distance between the returned corners. (khoảng cách Euclidean ở đây là đo bằng thước kẻ chứ không phải bằng số pixel ảnh)
corners = np.int0(corners)
print(corners)
for elem in corners:
    x, y = np.ravel(elem)   # np.ravel() function is aimed to Flatten the 2D matrix(elem in 3D corners_matrix) into 1D matrix   VD: [[1,2]] =>=> [1,2]
    cv2.circle(img, (x,y), 2, (0,255,0), -1)
img1 = cv2.dilate(img, kernel)
cv2.imwrite("ShiTomasi.png", img1)
cv2.imshow("Image", img)
cv2.waitKey()
cv2.destroyAllWindows()

