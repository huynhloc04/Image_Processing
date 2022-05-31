
#   LINK: https://stackoverflow.com/questions/54720646/what-does-ksize-and-k-mean-in-cornerharris
#         https://viblo.asia/p/corner-detection-voi-opencv-eW65Gv6YlDO

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("sodoku.png", cv2.IMREAD_GRAYSCALE)

#   =========================== LAPLACIAN METHOD =============================
#   Convert lap into the unsigned 8-bit integer
#   cv2.Laplacian() to find out the laplacian gradient of the image
Lap = cv2.Laplacian(img, cv2.CV_64F, ksize = 3)     #   Kích thước của kernel=5
#   cv2.cv_64F is a datatype which is 64 bit float and it supports the negative number when we'll deal with when laplacian method is running on image
Lap = np.uint8(np.absolute(Lap))
#   Take the absolute value of our laplacian image transformation and convert this value back to unsigned 8-bit integer cho phù hợp với cái output

#   =========================== SOBEL X =============================
Sobel_X = cv2.Sobel(img, cv2.CV_64F, 1, 0)     #   Tham số thứ 3 là: 1 <=> phương X,   0 <=> phương y
Sobel_Y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
#   Convert into unsigned 8-bit
Sobel_X = np.uint8(np.absolute(Sobel_X))
Sobel_Y = np.uint8(np.absolute(Sobel_Y))

#   Combine Sobel_X and Sobel_Y    ==>       ============= HIỆU QUẢ NHẤT ============
Combine_Sobel = cv2.bitwise_or(Sobel_X, Sobel_Y)        #   bitwise_or: kết hợp hai ảnh và làm rõ màu trắng (Ưu tiên màu trắng trong bitwise_or)

# ============================== Canny ===============================
#  The Canny Edge detection algorithm composed of 5 steps:
#    1. Noise reduction
#    2. Gradient calculation
#    3. Non_Maximum suppression
#    4. Double Threshold
#    5. Edge Tracking by Hysteresis
edges = cv2.Canny(img, 100, 200)
 
Titles = ["Origin_Image", "Laplacian", "Sobel_X", "Sobel_Y", "Combine_Sobel", "Canny"]
Images = [img, Lap, Sobel_X, Sobel_Y, Combine_Sobel, edges]
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(Images[i], "gray")
    plt.title(Titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()