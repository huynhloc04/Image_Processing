import cv2
import numpy as np
from matplotlib import pyplot as plt

def Non_Value(x):
    pass

def Camera_Canny():
    Camera_Id = 0
    cap = cv2.VideoCapture(Camera_Id)
    cv2.namedWindow("Canny_Window")
    cv2.createTrackbar("Min_Thresh", "Canny_Window", 0, 500, Non_Value)
    cv2.createTrackbar("MAX_Thresh", "Canny_Window", 0, 500, Non_Value)
    while(cap.isOpened()):
        ret, img = cap.read()
        if cv2.waitKey(10) == ord("q"):
            break
        if ret:
            min = cv2.getTrackbarPos("Min_Thresh", "Canny_Window")
            max = cv2.getTrackbarPos("MAX_Thresh", "Canny_Window")
            Canny_Image = cv2.Canny(img, min, max)
            cv2.imshow("Canny_Video", Canny_Image)
    cap.release()
    cv2.destroyAllWindows()

#   Hàm để xuất ra các hình ảnh bằng Matplotlib
def Show_Edge(Lap, Sobel_X, Sobel_Y, Combine_Sobel):
    Titles = ["Laplacian", "Sobel_X", "Sobel_Y", "Combine_Sobel"]
    Images = [Lap, Sobel_X, Sobel_Y, Combine_Sobel]
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(Images[i], "gray")
        plt.title(Titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

def Edge_Detection():
    Camera_ID = 0
    cap = cv2.VideoCapture(Camera_ID)
    while True:
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if cv2.waitKey(10) == ord("q"):
            break
        if ret:
            #   Laplacian Method
            Lap = cv2.Laplacian(img, cv2.CV_64F, ksize = 3)
            Lap = np.uint8(np.absolute(Lap))
            #   Sobel_XXXX Method
            Sobel_X = cv2.Sobel(img, cv2.CV_64F, 1, 0)
            Sobel_X = np.uint8(np.absolute(Sobel_X))
            #   Sobel_YYYY Method
            Sobel_Y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
            Sobel_Y = np.uint8(np.absolute(Sobel_Y))
            #   Sobel_x and Sobel_Y Combination
            Combine_Sobel = cv2.bitwise_or(Sobel_X, Sobel_Y)
            Show_Edge(Lap, Sobel_X, Sobel_Y, Combine_Sobel)
    cap.release()
    cv2.destroyAllWindows()
    

def main():
    Camera_Canny()
    Edge_Detection()

if __name__ == "__main__":
    main()