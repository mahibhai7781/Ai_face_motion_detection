import cv2
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model

def imotionDetect():
    face_classifier = cv2.CascadeClassifier('static/cascade/haarcascade_frontalface_default.xml')
    classfier = load_model('static/cascade/Emotion_Detection.h5')
    class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()  # captures frame and returns boolean value and captured image
        labels = []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.32, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + w, x:x + h]  # cropping region of interest i.e. face area from  image
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.10
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                preds = classfier.predict(roi)[0]
                label = class_labels[preds.argmax()]
                label_position = (x, y - 10)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                cv2.putText(frame, 'No Face Found', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Facial emotion Detection ', frame)
        key = cv2.waitKey(1)
        print("Welcome sir")
        if key == ord('e') or key == ord('E'):  # Check if 'e' key is pressed
            break
    cap.release()
    cv2.destroyAllWindows()

