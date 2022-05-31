import cv2
import numpy as np
img_1 = cv2.imread("Black_White.jpg")
img_2 = cv2.resize(img_1, (512,512))        #   cv2.resize(img, (width,height))
cv2.imshow("Half_Black_White", img_1)
img_2 = np.zeros((512,512,3), np.uint8)
cv2.rectangle(img_2, (156,156), (356,356), (255,255,255), -1)
cv2.imshow("Black_Image", img_2)

#   Phương thức bitwise_AND     white + anycolor = anycolor; black + anycolor = black 
bit_And = cv2.bitwise_and(img_1, img_2)
cv2.imshow("Bitwise_AND_Image", bit_And)

#   Phương thức bitwise_OR      Ưu tiên phần TRẮNG, những nơi nào giao nhau giữa vùng trắng và đen thì lấy TRẮNG
# bit_Or = cv2.bitwise_or(img_1, img_2)
# cv2.imshow("Bitwise_OR_Image", bit_Or)

#   Phương thức bitwise_XOR     Giao hai object khác màu => TRẮNG, giao hai object cùng màu => ĐEN
# bit_XOR = cv2.bitwise_xor(img_1, img_2)
# cv2.imshow("Bitwise_XOR_Image", bit_XOR)

#   Đảo TRẮNG => ĐEN, ĐEN => TRẮNG
# bit_not1 = cv2.bitwise_not(img_1)
# cv2.imshow("Bitwise_NOT_1", bit_not1)
# bit_not2 = cv2.bitwise_not(img_2)
# cv2.imshow("Bitwise_NOT_2", bit_not2)

cv2.waitKey()
cv2.destroyAllWindows()