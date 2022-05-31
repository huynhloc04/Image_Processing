import cv2
img = cv2.imread("Factory.jpg")
img_n = cv2.resize(img, dsize = None, fx = 0.5, fy = 0.5)
cv2.imshow("Aprilia Factory 1100 RSV4", img_n)
print("===============", img.size)
print("===============", img_n.size)
print("===============", img_n.dtype)
#   Ảnh đc lưu trên máy tính bằng cách gộp 3 ma trận 2 chiều lại vs nhau, mỗi mtr đại diện cho 1 màu đơn       
print("img", img[0])
#   Sd phương thức "split" để tách ảnh RGB thành 3 ảnh(3 ma trận) có 3 màu lần lượt là RED, GREEN, BLUE  
(b, g, r) = cv2.split(img)
#       b là ảnh chỉ có màu BLUE (ma trận ảnh màu xanh dương)
img_b = cv2.resize(b, dsize = None, fx = 0.5, fy = 0.5)
cv2.imshow("Resize_b", b)
#       g là ảnh chỉ có màu GREEN (ma trận ảnh màu xanh lá cây)
img_g = cv2.resize(g, dsize = None, fx = 0.5, fy = 0.5)
cv2.imshow("Resize_g", img_g)
#       r là ảnh chỉ có màu RED (ma trận ảnh màu đỏ)
img_r = cv2.resize(r, dsize = None, fx = 0.5, fy = 0.5)
cv2.imshow("Resize_r", img_r)
print(b)
print(g)
print(r)
#   Ghép 3 ảnh đơn màu lại ta được 1 ảnh RGB =>=> Sd phương thức "merge"
img_mr = cv2.merge((b, g, r))
cv2.imshow("Image", img_mr)
cv2.waitKey()
cv2.destroyAllWindows()


