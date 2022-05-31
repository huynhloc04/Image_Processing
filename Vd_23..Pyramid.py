
#   PURPOSE: Create a image with different resolutions. Then, we can search the object in image such as: face
#   These are 2 type of image pyramids      1. Gaussian_Pyramid     2. Laplacian_Pyramid
# import cv2
# img = cv2.imread("Lena512.jpg")
# cv2.imshow("Lena_Image", img)

# #   ============================ Gaussian Pyramid ============================
# #   There are 2 functions available for the Gaussian pyramid which is called "pyd_Down" and "pyd_Up"

# #   =>=>=> Pyd_Down Function <=<=<=
# lr_D = cv2.pyrDown(img)   #  ==> Reduce the resolution of an image 
# cv2.imshow("Pyr_Down", lr_D)  

# #   =>=>=> Pyd_Up Function <=<=<=
# lr_U = cv2.pyrUp(img)   #  ==> Reduce the resolution of an image 
# cv2.imshow("Pyr_Up", lr_U)

# layer = img.copy()
# #   Create a List to save pyramids
# Gauss_Lst = [layer]
# #   Create a For..loop to show the List of Pyramid
# for i in range(6):
#     layer = cv2.pyrDown(layer)
#     Gauss_Lst.append(layer)
#     cv2.imshow(f"{i}", layer)   #   Hàm imshow thì tham số đầu tiên phải là String


#   ============================ Laplacian Pyramid ============================

#       Với phương thức Laplacian, chỉ đc sử dụng những ảnh có kích thước : 256x256 / 512x512 / 1024x1024

import cv2
img = cv2.imread("Lena512.jpg")
cv2.imshow("Lena_Image", img)
layer = img.copy()
Gp_Lst = [layer]
#   Create a loop to find out the last image by using Laplacian_Pyramid
#   Các hình ảnh sau khi được scale down bằng cv2.pyrDown() được sắp xếp nhỏ dần từ 0->4 (5 ảnh gồm 1 ảnh layer gốc và 4 ảnh đc tạo trong For..loop)
for i in range(4):
    layer = cv2.pyrDown(layer)
    Gp_Lst.append(layer)

 #  Take the top level of the Gaussian pyramid -> is the last image of Gaussian_Pyramid in For..loop
Lapla_Lst = []

for i in range(len(Gp_Lst)-1, 0, -1):
    #   Scale_up từng hình ảnh và subtract ảnh đã scale_up vs ảnh gốc đó (Vd ScaleUp ảnh Gp_Lst[0](Sd cv2.pyrUp()), sau đó subtract ảnh đã
    #  scaleUp đó với cái ảnh Gp_Lst[0], cứ subtract lần lượt các ảnh Gp_Lst[i] trong vòng lặp For tuần tự như vậy -> Tạo ra một cái Laplacian)
    Gauss_Entend = cv2.pyrUp(Gp_Lst[i])
    #   Kích thước các ảnh trong Laplacian đc sắp xếp tăng dần từ 0->4 (5 ảnh gồm ảnh Gp_Lst[0] là ảnh cuối cùng của Gp_Lst và 4 ảnh trong vòng 
    #  vòng lặp For (đc tạo bằng cách cv2.subtract()))
    laplacian = cv2.subtract(Gp_Lst[i-1], Gauss_Entend)     #   Syntax: cv2.subtract(img_1, img_2)
    Lapla_Lst.append(laplacian)

for i in range(len(Lapla_Lst)):
    cv2.imshow(str(i), Lapla_Lst[i])

#   ======= Caution =======     When you increase the resolution after you have reduced the resolution, you're not going to get the same result
#                             as you might expect (The image you increase resolution after u havr reduced will be MỜ HƠN)
cv2.waitKey(0)
cv2.destroyAllWindows()