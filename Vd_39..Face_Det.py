
#   Link: https://github.com/opencv/opencv/tree/master/data/haarcascades
#         HAY =>=>=>=>=>=>https://sites.google.com/site/5kk73gpu2012/assignment/viola-jones-face-detection#TOC-Image-Pyramid
#         https://www.pyimagesearch.com/2021/04/12/opencv-haar-cascades/
#         Hay: https://hackaday.io/project/12384-autofan-automated-control-of-air-flow/log/41956-face-detection-using-a-haar-cascade-classifier
#         Object_Tracking and Object_Detection: http://datahacker.rs/001-opencv-projects-face-tracking-with-opencv-using-haar-cascade-detectors/
#         https://circuitdigest.com/tutorial/real-life-object-detection-using-opencv-python-detecting-objects-in-live-video
#         https://www.pyimagesearch.com/pyimagesearch-university/
#       Video minh hoa: https://vimeo.com/145874219?from=outro-embed
#                       https://vimeo.com/34545202?from=outro-embed
#                       https://vimeo.com/34545239?from=outro-embed
#         https://www.youtube.com/watch?v=_QZLbR67fUU
#         http://datahacker.rs/008-how-to-detect-faces-eyes-and-smiles-using-haar-cascade-classifiers-with-opencv-in-python/

import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
#smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        img_gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #   Sử dụng phương thức cv2.CascadeClassifier.detectMultiScale để detect khuôn mặt
        faces = face_cascade.detectMultiScale(img_gr, 1.1, 6, minSize = (60, 60))
        #       Syntax: cv2.CascadeClassifier.detectMultiScale(img, scaleFactor, minNeighbor)
        #                  - scaleFactor: Mỗi lần ảnh scale thì ảnh sau bằng (scaleFactor)% ảnh trước, đc sd trong Pyramid_Algorithm
        #                  - minNeighbor: Các detect_Window khi trượt qua 1 vùng mà có khả năng là khuôn mặt thì chúng sẽ vẽ các Wimdow 
        #                           lên ảnh, vùng càng có khả năng là khuôn mặt thì sẽ có càng nhiều Window, tập hợp các Window như vậy đgl Neighbor. 
        #                           Vì vậy, chúng ta set giá trị minNeighbor này để quy định "vùng sẽ là khuôn mặt khi và chỉ khi vùng đó có số 
        #                           Neighbor_Wimdow ít nhất là giá trị minNeighbor", những vùng có minNeighbor nhỏ hơn g.trị này thì ko chứa khuôn mặt và sẽ bị bỏ qua. 
                       
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            #   Sử dụng p.pháp ROI để cắt ảnh (Cắt cái detect window chứa khuôn mặt)
            #       ROI ảnh xám từ img_gr
            roi_gr = img_gr[y:y+h, x:x+w]
            #       ROI ảnh màu từ frame
            roi_color = frame[y:y+h, x:x+w]
            #   Sử dụng phương thức cv2.CascadeClassifier.detectMultiScale để detect mắt
            eyes = eye_cascade.detectMultiScale(roi_gr)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,255), 2)
            # smiles = smile_cascade.detectMultiScale(roi_color, 1.8, 7)
            # for (sx, sy, sw, sh) in smiles:
            #     cv2.rectangle(roi_color, (sx,sy), (sx+sw, sy+sh), (0,0,255), 2)
            cv2.imshow("Image", frame)
    if cv2.waitKey(5) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()




