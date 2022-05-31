
#       Túm cái váy lại thì BackProjection là 1 phương thức  tạo ra 1 cái MASK mà phần trắng của cái mask là đối tượng mà ta muốn. Bằng cách sd Histgram của 
#   ảnh mẫu (đc cắt ra từ ảnh gốc), ta sẽ tìm đc các pixel tương tự trong ảnh gốc, tập hợp các pixel tương tự đó, ta có 1 cái mask.

import cv2
import numpy as np 
from matplotlib import pyplot as plt 
Ori_Img = cv2.imread("Back_Pro_Goaler.jpg") 
ROI = cv2.imread("Back_Pro_Grass.jpg")
#   Convert Ori_Img to HSV Space
HSV_Ori = cv2.cvtColor(Ori_Img, cv2.COLOR_BGR2HSV)
HSV_ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2HSV)
#   Take the Histogram of ROI
ROI_Hist = cv2.calcHist([HSV_ROI], [0, 1], None, [180, 256], [0, 180, 0, 256])
#   Create a BackProject (MASK)
Mask = cv2.calcBackProject([HSV_Ori], [0, 1], ROI_Hist, [0, 180, 0, 256], 1)
#   Mask have some noises, we use Filter to remove noise
# cv2.dilate(Mask, None, iterations = 2)
# cv2.imshow("Mask", Mask)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
Mask = cv2.filter2D(Mask, -1, kernel)
#   Use Threshold to create binary_image
_, Mask = cv2.threshold(Mask, 60, 255, cv2.THRESH_BINARY)
#   Convert 2D image to 3D image to use Bitwise_and method. Two image in Bitwise_and() is 3D image. 
Mask = cv2.merge((Mask, Mask, Mask))
result = cv2.bitwise_and(Mask, Ori_Img)
cv2.imshow("Mask_Dilation", result)
cv2.waitKey()
cv2.destroyAllWindows()
