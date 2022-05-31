# import cv2
# import numpy as np
# img = cv2.imread("Ballon.jpg")
# #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # _, Thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
# # cv2.imshow("Thresh", Thresh)

# # kernal = np.ones((3,3), np.uint8)
# # Dilation = cv2.dilate(Thresh, kernal, iterations = 1)

# # #blur = cv2.GaussianBlur(gray, (3,3), 0)
# # Blur = cv2.bilateralFilter(Thresh, 9, 75, 75)
# # cv2.imshow("Blur", Blur)
# # #   Tìm cạnh của Object trong hình bằng cv2.Canny =>=> Làm mượt cạnh
# edge = cv2.Canny(img, 100, 200)
# cv2.imshow("Canny_Edge", edge)
# # Lap = cv2.Laplacian(Thresh, cv2.CV_64F, ksize = 3)
# # Lap = np.uint8(np.absolute(Lap))
# contours, _ = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# #draw = cv2.drawContours(img, contours, -1, (0,255,0), 2)
# # cv2.imshow("Drawed_Contour", draw)
# dem = 0
# for contour in contours:
#     (x, y, width, height) = cv2.boundingRect(contour)
#     if cv2.contourArea(contour) < 1000:
#         continue
#     dem += 1
#     cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0), 2)
# print(dem)
# cv2.imshow("Ballon_Contours", img)
# cv2.waitKey()
# cv2.destroyAllWindows()




import cv2
import imutils
img = cv2.imread('Ballon.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thres = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,21,10)

contours = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=False)

number = 0
# loop over our contours
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    print(x, y, w, h)
    #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # approximate the contour
    if (85<w<150) and(100<h<150):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        number +=1

print("Number of Contours found = " + str(number))
#cv2.drawContours(img, contours, -1, (0, 255, 0), 3)


cv2.imshow('Pix',img)
#cv2.imshow('Thres',thres)
cv2.waitKey()
cv2.destroyAllWindows()