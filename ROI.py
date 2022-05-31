
import cv2

#   Hàm tìm tọa độ của điểm khi click chuột
def Mouse_Back(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = f"[{y};{x}]"
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.circle(img_rs, (x,y), 3, (0,0,255), -1)
        cv2.putText(img_rs, text, (x+10,y-10), font, 0.55, (0,0,255), 1, cv2.LINE_AA)
        
#   Hàm sao chép 1 object trong ảnh (ROI) => Sao chép quả bóng và dán chỗ khác
def Copy_Ball(img_rs):
    #   ========================= Syntax: ROI = img[{y1}:{y2}, {x1}:{x2}] =========================
    ball = img_rs[24:192, 246:415]
    img_rs[292:460, 121:290] = ball
    img_rs[70:238, 816:985] = ball
    cv2.imshow("Ball_ROI", ball)

def Reg_Face(img_rs):
    cv2.rectangle(img_rs, (467,10), (577,128), (0,255,0), 1)
    cv2.imshow("Messi with Ball", img_rs)

#   Hàm ghép 2 ảnh chồng lên nhau
def Ghep_Anh(img, img_2):
    #   hai ảnh ghép vào phải có cùng kích thước, nếu ko cùng thì sd phương thức "resize" để 2 ảnh bằng nhau
    img = cv2.resize(img, (512,512))
    img_2 = cv2.resize(img_2, (512,512))
    #   Ghép 2 ảnh
    dst = cv2.add(img, img_2)
    cv2.imshow("Messi with Ball", dst)

#   Phương thức addWeighted (ghép 2 ảnh, ảnh nào bạn muốn rõ hơn, hình ảnh rõ hơn => addWeighted)
#   Syntax: addWeighted(img_1, alpha, img_2, beta, gamma)   alpha: tỉ lệ ảnh 1 xuất hiện, beta: tỉ lệ ảnh 2 xuất hiện
def addWeighteddd(img, img_2):
    #   hai ảnh ghép vào phải có cùng kích thước, nếu ko cùng thì sd phương thức "resize" để 2 ảnh bằng nhau
    img = cv2.resize(img, (512,512))
    img_2 = cv2.resize(img_2, (512,512))
    #   Ghép 2 ảnh
    dst = cv2.addWeighted(img, .2, img_2, .8, 0)
    cv2.imshow("Messi with Ball", dst)

img = cv2.imread("Messi.jpg")
img_2 = cv2.imread("Kawa_ZX10R.png")
img_rs = cv2.resize(img, dsize = None, fx = 0.7, fy = 0.7)
#cv2.imshow("Messi with Ball", img_rs)
#cv2.setMouseCallback("Messi with Ball", Mouse_Back)
Copy_Ball(img_rs)
#Reg_Face(img_rs)
#cv2.imshow("Messi with Ball", img_rs)
#Ghep_Anh(img, img_2)
#addWeighteddd(img, img_2)
cv2.waitKey()
cv2.destroyAllWindows()
