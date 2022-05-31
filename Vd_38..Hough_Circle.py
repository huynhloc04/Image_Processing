
#   HoughCircles_Transform explain:  1. https://www.youtube.com/watch?v=Ltqt24SQQoI
#                                    2. http://datahacker.rs/opencv-circle-detection-hough-transform/
#                                    3. https://www.youtube.com/watch?v=-o9jNEbR5P8 All links in the description
#                                    4. https://learnopencv.com/hough-transform-with-opencv-c-python/
#                                    5. https://docs.opencv.org/2.4/modules/imgproc/doc/feature_detection.html?highlight=houghcircles

#   Step 1. Chuyển ảnh sang ảnh xám
#   Step 2. Sử dụng cv2.GaussianBlur để làm mờ ảnh
#   Step 3. Sử dụng cv2.HoughCircles để detect đ.tròn
#   Step 4. Vẽ các đ.tròn với tâm và bán kính đã đc return từ hàm cv2.HoughCircles()


import numpy as np 
import cv2

def nothing():
    pass

img_st = cv2.imread("Color_Ball.jpg")
img = cv2.resize(img_st, (820,730))
print(img.shape)
#   Convert img to gray image
img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#   Làm mờ ảnh để giải thuật HoughCircles bỏ qua những h.tròn lỗi (không phải h.tròn nhưg lại có hình tương tự h.tron)
Gblur = cv2.GaussianBlur(img_gr, (5,5), 0)

#   ================================ Create TRACKBAR to find out Upper_Threshold for Canny detect =================================
# cv2.namedWindow("Tracking")
# cv2.createTrackbar("minVal", "Tracking", 0, 300, nothing)
# cv2.createTrackbar("maxVal", "Tracking", 0, 400, nothing)
# while True:
#     if cv2.waitKey(10) == ord("q"):
#         break
#     minVal = cv2.getTrackbarPos("minVal", "Tracking")
#     maxVal = cv2.getTrackbarPos("maxVal", "Tracking")
#     Edge = cv2.Canny(Gblur, minVal, maxVal)
#     cv2.imshow("Edge_Image", Edge)


#   Use HoughCircles method to detect circle
Circles = cv2.HoughCircles(Gblur, cv2.HOUGH_GRADIENT, 1, 50, param1 = 192, param2 = 10, minRadius = 40, maxRadius = 80)
if Circles is not None:
    Circles = np.round(Circles).astype("int")
    for elem in Circles[0, : ]:     #   Lấy m.trận_0 (1 cái mảng 2 chiều) trong m.trận 3 chiều, và lấy tất cả các hàng và cột trong m.trận 0 đó
        cv2.circle(img, (elem[0], elem[1]), elem[2], (200,0,0), 3)  #  Vẽ đ.tròn
        cv2.circle(img, (elem[0], elem[1]), 2, (200,0,0), -1)       #  Vẽ tâm đ.tròn 
cv2.imshow("HoughCircles Transform Image", img)
cv2.waitKey()
cv2.destroyAllWindows()


#   ======================================== HoughCircles Transform Syntax Explain ======================================

#         Circles = cv2.HoughCircles(img, method, dp, minDist, param1, param2, minRadius, maxRadius)
#   Hàm này sẽ trả về 1 m.trận 3 chiều chứa lần lượt tọa độ x, tọa độ y, bán kính r


#  1. img     : Ảnh đầu vào cần Detect
#  2. method  : Phương pháp sử dụng để detect đường tròn      =>=> cv2.HOUGH_GRADIENT
#  3. dp      : Thuật toán sẽ tạo ra 1 accumulator (Ảnh tích trữ) và chia accumlator đó thành nhiều pixel nhỏ bằng số pixel của ảnh gốc (nếu dp=1), nhỏ hơn 1 nửa so vs số pixel ảnh gốc (nếu dp=2)
#     Mục đích của việc tạo accumulator này là để chia ảnh ra từng pixel nhỏ, mỗi pixel sẽ đảm nhận việc xem xét thử bản thân pixel có chứa tâm của đ.tron ko?
#     Thuật toán sẽ tạo 1 "đ.tròn_quét" và tâm của nó sẽ quét dọc theo cạnh của ảnh đã đc Edge_Detect, nếu tại pixel nào chứa số giao điểm của các đ.tròn đó niều nhất, thì pixel của accumulator đó sẽ chứa tâm đ.tròn 
#     nếu ko có giao điểm nào lớn nhất, tức là vòng tròn chưa = b.kính của vòng tròn tìm, thuật toán sẽ tăng b.kính của "đ.tròn_quét" lên 1 pixel và tiếp tục thực hiện công việc như vậy cho đến khi tìm đc pixel có 
#     số giao điểm của các đ.tròn nhiều nhất ==> Tâm của đ.tròn (Các "đ.tròn_quét" sẽ được tăng bán kính từ bán kính nhỏ nhất "minRadius" đến "maxRadius"), nếu đã tăng đến "maxRadius" mà vấn chưa tìm thấy pixel có số 
#     giao điểm nhiều nhất, thoát khỏi cái edge đó => ko phải đ.tròn và chuyển qua "quét" edge khác. 
#      Bản chất của accumulator là 1 cái ảnh_tích_lũy mà mỗi pixel của ảnh thực hiện đếm số lượng giao điểm của các "đ.tròn_quét", pixel nào có giá trị (số giao điểm) lớn nhất => pixel đó chứa tâm đ.tròn,
#  4. minDist : khoảng cách nhỏ nhất giữa tâm các đ.tròn, nếu minDist này QUÁ NHỎ thì sẽ càng NHIỀU các đường tròn ảo (các đ.tròn mà ta không muốn detect) sẽ được detect.
#     nếu minDist này QUÁ LỚN, thì sẽ có 1 số đ.tròn sẽ bị bỏ sót, nhớ rằng trong ảnh mặc dù ta đã sd Edge_Detect nhưng vẫn x.hiện nhiều đ.cong như đ.tròn, thuật toán sẽ hiểu nhầm là đường tròn và xuất ra k.quả detect luôn, 
#     nên trong hàm cv2.HoughCircles có rất nhiều tham số hỗ trợ nhau để Detect đúng đc đ.tròn
#  5. param1  : Là giới hạn trên (Upper_Threshold) cho Canny_Edge Detect, còn Lower_Thhreshold thì bằng 1 nửa của Upper_Threshold  ==> cv2.Canny(img, Upper_Threshold, Lower_Threshold)
#  6. param2  : Là ngưỡng giới hạn giao điểm của tâm đ.tròn, các đường tròn nào có tâm (số giao điểm của các đ.tròn quét) LỚN hơn ngưỡng này mới đc chấp nhận, không thì sẽ bị bỏ qua
#     (tham số này rất hữu ích trong trường hợp các Edge là đường cong ko kín, vì số g.điểm của các đ.tròn quét trên đ.cong này không lớn hơn ngưỡng param2 này nên ko đc chấp nhận)
#  7. minRadius: bán kính NHỎ NHẤT của đ.tròn muốn detect (những đ.tròn có bán kính NHỎ hơn ngưỡng này sẽ ko ddc chấp nhận)
#  8. maxRadius: bán kính LỚN NHẤT của đ.tròn muốn detect (những đ.tròn có bán kính LỚN hơn ngưỡng này sẽ ko ddc chấp nhận)





