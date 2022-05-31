
#   cv2.arcPolyDF LINK: https://www.programmersought.com/article/66174553670/

import cv2
img = cv2.imread("Shape.jpg")
img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, Thresh = cv2.threshold(img_gr, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(Thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    #   1. First argument : is a curve ==> the cnt in contours
    #   2. Second argument: EPSILON: this argument is a parameter specifying the approximation accuracy
    #         define EPSILON: 0.01*cv2.arcLength(cnt, closed)     Method cv2.arcLength() caculates cnt (a contour) parameter or a cur ve LENGTH
    #          - "cnt"   : is the single contour value entered (cnt in contours)
    #          - "closed": True if the shape is Closed (hình khép kín), False if the shape is Opened
    #   3. Third argument: True indicates that the contour is closed

    epsilon = 0.009*cv2.arcLength(cnt, True)        #   Calculate the circumference of the contour
    # cv2.approxPolyDF trả về các tọa độ đỉnh của các Polygon hay Curve, biến "approx" lưu 1 cái mtr chứa các tọa độ đỉnh của hình
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    print("=================",len(approx))
    # print(approx)
    cv2.drawContours(img, [approx], 0, (0,255,0), 2)
    #   approx.ravel() lưu 1 cái List chứa chung tọa độ x,y các đỉnh của hình. VD Rectangle: approx.ravel() = [xA yA xB yB xC yC xD yD] ==> approx.ravel()[0]=xA, approx.ravel()[1]=yA
    #   Đặt Text tại vị trí đỉnh (x,y) = (approx.ravel()[0], approx.ravel()[1]) của hình
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    #   putText on image
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x-25, y-7), font, 0.5, (0,0,0), 1, cv2.LINE_AA)
cv2.imshow("Geometric_Shape", img)
cv2.waitKey()
cv2.destroyAllWindows()




# 1. cv2.contourArea(cnt， oriented = False)  # Calculate the area of ​​the contour
#  Parameter description: cnt is the single contour value entered; Oriented:The default value is false, oriented to regional identifiers,
#  If true, returns a signed area, depends on the direction of the contour(Clockwise: gtri dương nếu cùng chiều KDH or counterclockwise: âm nếu ngược KDH).
#  If the default value is False, the area is returned as an absolute value (Trả về giá trị diện tích của Contour đó_ là 1 con số)

# 2. cv2.arcLength(cnt， closed)   # Calculate the circumference of the contour
#  Parameter description: cnt is the single contour value entered,closed means that the shape used to specify the object is
#  Closed (True), still an open curve(False)。 

# 3. cv2.aprroxPolyDP(cnt, epsilon， True)  # Used to obtain the approximate value of the contour, use cv2.drawCountors for drawing operations
#    Parameter description: cnt is the input profile value, epsilon is the threshold T,
#    Usually the perimeter of the contour is used as the threshold,TrueIndicates that the contour is closed

# 4. x, y, w, h = cv2.boudingrect(cnt) # Trả về các tọa độ (x,y) trái & phải trên cùng, chiều dài, chiều rộng của rectangle gần sát vs viền ảnh nhất
#  Parameter description: x, y, w,  h represents the x-axis and y-axis coordinates of the circumscribing rectangle,
#  And the width and height of the rectangle, cnt represents the input contour value

# 5. (x, y), radius = cv2.minEnclosingCircle(cnt) # Trả về tọa độ tâm và bán kính of đường tròn gần nhất với viền ảnh của object
#  Parameter Description: (x, y) represents the "center" of the circle, radius represents the radius of the circumcircle, cnt represents single contour

