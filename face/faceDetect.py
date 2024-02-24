import cv2
import numpy as np
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
from keras.models import load_model
def faceDetect():
    face_classfier = cv2.CascadeClassifier('static/cascade/haarcascade_frontalface_default.xml')
    classfier =load_model('static/cascade/./Emotion_Detection.h5')

    class_labels=['Angry','Happy','Neutral','Sad','Surprise']

    img=cv2.imread("static/images/Bhai.jpg")
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_classfier.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+w,x:x+h]#cropping region of interest i.e. face area from  image
        roi_gray=cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray])!=0:
            roi=roi_gray.astype('float')/255.10
            roi=img_to_array(roi)
            roi=np.expand_dims(roi,axis=0)

            preds=classfier.predict(roi)[0]
            label=class_labels[preds.argmax()]
            label_position=(x,y-10)
            cv2.putText(img,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        else:
            cv2.putText(img,'No Face Found', (20,60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow('Facial emotion Detection ',img)
    key = cv2.waitKey(0)
    if key == ord('e'):  # Check if 'e' key is pressed
        cv2.destroyAllWindows()
