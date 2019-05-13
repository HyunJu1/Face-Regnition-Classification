import cv2
import random
import glob

face_cascade = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_default.xml')
eye_casecade = cv2.CascadeClassifier('./haarcascade/haarcascade_eye.xml')

image_name = glob.glob('D:\DeepLearning_Project\image1/*.jpg')
for i in image_name:
    img = cv2.imread(i)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    imgNum  = 0
    for (x,y,w,h) in faces:
        cropped = img[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]
        # 이미지를 저장
        s= random.random()
        cv2.imwrite("./outputs/thumbnail" + str(s) + ".png", cropped)
        imgNum += 1

    #cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    # roi_gray = gray[y:y+h, x:x+w]
    # roi_color = img[y:y+h, x:x+w]
    # eyes = eye_casecade.detectMultiScale(roi_gray)
    # for (ex, ey, ew, eh) in eyes:
    #     cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)

#cv2.imshow('Image view', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
