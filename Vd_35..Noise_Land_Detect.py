# import cv2
# from matplotlib import pyplot as plt 
# import numpy as np

# def Edge_Detect(img):
#     img_plt = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     Gblur = cv2.GaussianBlur(img_plt, (5,5), 0)
#     edge = cv2.Canny(Gblur, 310, 400)
#     return edge

# def Create_Mask(img):
#     height = img.shape[0]
#     width = img.shape[1]
#     Pentagons = np.array([
#         [0, height], 
#         [width, height], 
#         [width, 235],
#         [int(width/2), 45],
#         [0, 250]         ])
#     mask = np.zeros_like(img)
#     cv2.fillPoly(mask, [Pentagons], (255,255,255))
#     return mask

# def Hough_Trans(img, origin_img):
#     lines = cv2.HoughLinesP(img, 1, np.pi/180, 8, minLineLength = 2, maxLineGap = 10)
#     for line in lines:
#         x1, y1, x2, y2 = line[0]
#         cv2.line(origin_img, (x1,y1), (x2,y2), (0,255,0), 1)
#     return origin_img

# def main():
#     img = cv2.imread("Highway.jpg")
#     Edge_Img = Edge_Detect(img)
#     Mask = Create_Mask(Edge_Img)
#     # cv2.imshow("Mask_Image", Mask)
#     # cv2.imshow("Edge_Image", Edge_Img)
#     # plt.imshow(img)
#     # plt.show()
#     Bitwise_Img = cv2.bitwise_and(Edge_Img, Mask)
#     cv2.imshow("Bitwise", Bitwise_Img)
#     Hough_Img = Hough_Trans(Bitwise_Img, img)
#     cv2.imshow("Hough_Transform", Hough_Img)
#     cv2.waitKey()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()



#         ============================== Reduce Noise in Detect Land_Traffic =============================

import cv2
import matplotlib.pyplot as plt 
import numpy as np 

def Edge_Detect(img):
    img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    Gblur = cv2.GaussianBlur(img_gr, (5,5), 0)
    edge = cv2.Canny(Gblur, 126, 308)
    return edge

def Create_Mask(img):
    mask = np.zeros_like(img)
    print(mask.shape)
    Geo_Shape = np.array([
        [0, 720],
        [1200, 720],
        [632, 515],
        [0, 660]        ])
    cv2.fillPoly(mask, [Geo_Shape], (255,255,255))
    return mask

def Hough_Trans(Bitwise, frame):
    lines = cv2.HoughLinesP(Bitwise, 1, np.pi/180, 10, minLineLength = 8, maxLineGap = 3)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1,y1), (x2,y2), (0,0,255), 1)
    return frame

def nothing():
    pass

def Cap_Read():
    # cv2.namedWindow("Tracking")
    # cv2.createTrackbar("minVal", "Tracking", 0, 700, nothing)
    # cv2.createTrackbar("maxVal", "Tracking", 0, 700, nothing)
    cap = cv2.VideoCapture("Vd_35_Highway.mp4")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if cv2.waitKey(10) == ord("q"):
            break
        if ret:
            # minVal = cv2.getTrackbarPos("minVal", "Tracking")
            # maxVal = cv2.getTrackbarPos("maxVal", "Tracking")
            Edge = Edge_Detect(frame)
            cv2.imshow("EDGE", Edge)
            Mask = Create_Mask(Edge)
            Bitwise = cv2.bitwise_and(Edge, Mask)
            cv2.imshow("Bitwise_and", Bitwise)
            Final = Hough_Trans(Bitwise, frame)
            cv2.imshow("Land_Highway_Detect!!!", Final)
    cap.release()
    cv2.destroyAllWindows()

def main():
    Cap_Read()

if __name__ == "__main__":
    main()


