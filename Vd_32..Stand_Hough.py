#       The Hough_Transform is a popular technique to DETECT ANY SHAPE if u can represent that shape in a MATHEMATICAL form. It can detect the
#   shape even if it's broken or distored a little bit.  It keeps track of the intersection between curves of every point in the image.

#       Những điểm nằm trên cùng một đường thẳng (hay nằm cùng chung 1 chu vi hình học), thì những đường cong (mỗi đường cong biểu diễn cho 1 điểm)
#   trong kh.gian (r, 0) giao nhau tại cùng 1 điểm. 

#      Ban đầu, giải thuật sẽ tìm và xét từng cái edge trong ảnh Edge (vừa tạo bằng cv2.Canny()), nếu tất cả những cái điểm trong cái edge riêng rẽ đó 
#   có đồ thị giao nhau tại cùng 1 điểm thì PHẦN HÌNH HỌC thỏa điều kiện này của edge sẽ là 1 đt. Như vậy, nếu trong 1 ảnh có 1 đường thẳng 
#   (mỗi đường thẳng là tập hợp của nhìu điểm, mỗi điểm được biểu diễn bởi 1 đường cong trong không gian (c,m)) nhiều đường cog giao nhau tại 1 điểm, 
#   mà nếu SỐ LƯỢNG đg.cong trên 1 ngưỡng Threshold nào đó, thì chắc chắn tập hợp những điểm đó sẽ là 1 đường thẳng với độ dài thỏa yêu cầu (số điểm pixel của đt > Threshold)

#   Detail about Hough_Transform:  https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
#   Python Implementaton: https://moonbooks.org/Articles/Implementing-a-simple-python-code-to-detect-straight-lines-using-Hough-transform/

import cv2
import numpy as np
img = cv2.imread("Sodoku.jpg")
img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Edge = cv2.Canny(img_gr, 40, 100)
#cv2.imshow("Image_Gray", img_gr)
cv2.imshow("Image_Canny", Edge)
#     Standard Hough Transform         =>=>=>=>=>=>=>=>=>=> SYNTAX:   lines = cv2.HoughLines(img, rho, theta, threshold)
#     cv2.HoughLines() gives you a LIST_(lines), each element in LIST_(lines) contains a vector of couples (bán kính r, góc 0)
#   each element represent for an line in IMAGE (Because each elemt (r,0) is a line in (c,m) coordinate system)
lines = cv2.HoughLines(Edge, 1, np.pi/180, 168)
for line in lines:
    rho = line[0][0]
    theta = line[0][1]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = rho*a
    y0 = rho*b
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)
cv2.imshow("Hough_Transform",img)
cv2.waitKey()
cv2.destroyAllWindows()



