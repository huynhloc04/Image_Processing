
#   Kind of filter: Homogeneous_Filter, Gassian_Filter, Median_Filter, Bilateral_Filter
import cv2
from matplotlib import pyplot as plt
import numpy as np

img_st = cv2.imread("OpenCV.png")   #   ==> Chuyển về ảnh xám(nếu ảnh nguồn là ảnh trắng đen, chyển về hệ RGB nếu ảnh nguồn là ảnh màu) 
#                                   vì Matplotlib chỉ đọc ảnh RGB while OpenCv đọc ảnh BGR
img = cv2.cvtColor(img_st, cv2.COLOR_BGR2RGB)
kernel = np.ones((5,5), np.float32)/25

#   Homogeneous_Filter: Lọc đồng nhất ==> Làm giảm hiện tượng răng cưa tại các chỗ cong của image

#   ddepth -1 params explaination LINK: https://stackoverflow.com/questions/43392956/explanation-for-ddepth-parameter-in-cv2-filter2d-opencv
dst = cv2.filter2D(img, -1, kernel)
 
#   Blur 
blur = cv2.blur(img, (4,4)) # (4,4): Kích thước của Kernel

#   Gassian_Filter
Gblur = cv2.GaussianBlur(img, (5,5), 0)

#   Salt and Peper noise    ==> Median Blur Method
Median_Blur = cv2.medianBlur(img, 3)

#   Bilateral Filter: Làm mờ ảnh -> giảm răng cưa đồng thời giữ đc độ sắc của các cạnh của object trong hình
Bilation = cv2.bilateralFilter(img, 10, 75, 75)  # 9: diameter of each pixel, 75: sigma color, 75: sigma space

Titles = ["Origin_Image", "Homogeneous_Filter", "BLUR", "GassianBlur", "Median_Blur", "Bilateral"]
Images = [img, dst, blur, Gblur, Median_Blur, Bilation]
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(Images[i], "gray")
    plt.title(Titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()