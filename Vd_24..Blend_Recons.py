

#       Using Pyramid to blend 2 image by 5 steps:
#   1. Load the 2 images of apple and orange
#   2. Find the Gaussian Pyramids for apple and orange (in this particular example, number of levels is 6)
#   3. From Gaussian Pyramid => find their Laplacian Pyramid
#   4. Now jjoin the left half of apple and right of orange in each levels of Laplacian Pyramid
#   5. Finally, from this jonit image pyramid, reconstruct the original image


import cv2
import numpy as np
apple = cv2.imread("Apple.jpg")
orange = cv2.imread("Orange.jpg")
#   Step number 2: Find the Gaussian_Pyramid
apple_copy = apple.copy()
orange_copy = orange.copy()
App_Lst = [apple_copy]
Org_Lst = [orange_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    App_Lst.append(apple_copy)
    orange_copy = cv2.pyrDown(orange_copy)
    Org_Lst.append(orange_copy)

#   Step number 3: Convert Gaussian_pyramid to Laplacian_Pyramid
Lapla_App_Lst = [App_Lst[-1]]
Lapla_Org_Lst = [Org_Lst[-1]]
for i in range(len(App_Lst)-1, 0, -1):  #  len(App_Lst) hoặc len(Org_Lst) cũng OK hết
    #   Apple
    Gauss_Extend_App = cv2.pyrUp(App_Lst[i])
    Lapla_App = cv2.subtract(App_Lst[i-1], Gauss_Extend_App)
    Lapla_App_Lst.append(Lapla_App)
    #   Orange
    Gauss_Extend_Org = cv2.pyrUp(Org_Lst[i])
    Lapla_Org = cv2.subtract(Org_Lst[i-1], Gauss_Extend_Org)
    Lapla_Org_Lst.append(Lapla_Org)

#   Step number 4: Add left and right halves of images in each level
Apple_Orange = []
for i in range(len(Lapla_App_Lst)):   #  len(App_Lst) hoặc len(Org_Lst) cũng OK hết
    #   Chiều dài của ảnh thay đổi, vì mỗi ảnh trong LaplaLst có kích thước khác nhau
    _, width, _ = Lapla_App_Lst[i].shape
    Blend = np.hstack((Lapla_App_Lst[i][:,:int(width/2)], Lapla_Org_Lst[i][:,int(width/2):]))
    Apple_Orange.append(Blend)

#   Step number 5: Reconstruct image
App_Org_Recons = Apple_Orange[0]
for i in range(1, len(Apple_Orange)):
    App_Org_Recons = cv2.pyrUp(App_Org_Recons)
    App_Org_Recons = cv2.add(Apple_Orange[i], App_Org_Recons)

cv2.imshow("Apple", apple)
cv2.imshow("Orange", orange)
apple_orange = np.hstack((apple[:,:256], orange[:,256:])) 
cv2.imshow("Simple_Blend", apple_orange)
cv2.imshow("Pyramid_Blend", App_Org_Recons)

cv2.waitKey()
cv2.destroyAllWindows()