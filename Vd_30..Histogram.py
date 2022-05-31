
# #       Histograms LINK: https://docs.opencv.org/master/d1/db7/tutorial_py_histogram_begins.html
# #   Histogram is a plot with pixel values (ranging from 0 to 255 (từ ĐEN đến TRẮNG), not always) trên trục X và số lượng pixel ảnh trên trục Y.

# #   =>=>=>=>=>=>=>=>=>=>  Histogram is drawn for GRAYSCALE image, NOT color image  <=<=<=<=<=<=<=<=<=
# #   Trục ĐỨNG thể hiện SỐ LƯỢNG pixel của ảnh ứng với trục cường độ màu nằm ngang
# #   Trục nằm ngang thể hiện cường độ của màu của ảnh xám, từ 0 -> 255

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# #img = np.zeros((256,256,3), np.uint8)
# img = cv2.imread("Lena512.jpg")
# img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Image", img_gr)
# #   Find out histogram (biểu đồ) of the image using matplotlib
# #       plt.hist which calculates the histogram of an image
# #     -  First argument is source_image
# #     -  Second argument is maximum number of pixel value => 255 (Số lượng các giá trị có thể có của ảnh => có 256 gtri)
# #     -  Third argument_It is the range of intensity values you want to measure. Normally, it is [0,255].
# plt.hist(img_gr.ravel(), 256, [0,255])
# plt.show()
# cv2.waitKey()
# cv2.destroyAllWindows()


# # ===================  Histograms with BGR color  =======================

# import cv2
# from matplotlib import pyplot as plt
# img = cv2.imread("CBR.png")
# (B, G, R) = cv2.split(img)       #   =============== cv2.split() =================
# cv2.imshow("Blue", B)
# cv2.imshow("Green", G)
# cv2.imshow("Red", R)
# plt.hist(B.ravel(), 256, [0,255])
# plt.hist(G.ravel(), 256, [0,255])
# plt.hist(R.ravel(), 256, [0,255])
# plt.show()
# cv2.waitKey()
# cv2.destroyAllWindows()


#  ========================  Histogram Calculation in OpenCV  =====================

import cv2
import numpy as np
from matplotlib import pyplot as plt
img_st = cv2.imread("CBR.png", 0)
img_n = cv2.resize(img_st, (760, 512)) #   (width, height)
#  Create MASK
mask = np.zeros((512, 760), np.uint8)
cv2.rectangle(mask, (150,250), (600, 450), (255), -1)
cv2.imshow("Mask_Image", mask)
# Img_Bit = cv2.bitwise_or(img_n, mask)
# cv2.imshow("Bitwise_Image", Img_Bit)
hist = cv2.calcHist([img_n], [0], mask, [256], [0,256])
    #    - [img] : source_image. It should be given in square brackets
    #    - [0]   : - It is the index of channel for which we calculate histogram. For example, if input is GRAYSCALE image, its value is [0].
    #  For COLOR image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively. 
    #              - If we use HSV color space, it's only one channel is H (Hue). Hence, we set this argument is [0].
    #    - mask  : mask_image. To find histogram of full image, it is given as "None". But if u want to find histogram of particular region of image, 
    #  you have to create a mask_image for that and give it as mask.
    #    - [256] : histSize => We have 256 color value go from 0 to 255 => We set this argument is [256]. But in HSV color space, we have only 
    #                        180 value go from 0 to 179. Thus, we set this argument is [180]
    #    - [0,256]: The RANGE (It is the range of intensity values you want to measure. Normally, it is [0,255]). But in HSV color space, we set [0, 180]
plt.plot(hist)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()