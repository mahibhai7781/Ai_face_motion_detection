import cv2
import numpy as np
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
from keras.models import load_model

# Function to detect emotions in video stream
def VideoImotionDetection():
    # Load Haar cascade for face detection
    face_classifier = cv2.CascadeClassifier('static/cascade/haarcascade_frontalface_default.xml')

    # Load the pre-trained emotion detection model
    classifier = load_model('static/cascade/Emotion_Detection.h5')
    class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']

    # Capture video from the webcam
    cap = cv2.VideoCapture("static/images/BhaiVideo.mp4")

    # Reduce the webcam resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Width
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Height

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # Draw rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Extract ROI (Region of Interest) for emotion detection
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                # Preprocess ROI for emotion detection
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                # Predict emotion
                preds = classifier.predict(roi)[0]
                label = class_labels[preds.argmax()]

                # Display emotion label
                label_position = (x, y - 10)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                cv2.putText(frame, 'No Face Found', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Display the resulting frame
        cv2.imshow('Facial Emotion Detection', frame)

        # Exit the loop when 'e' key is pressed
        key = cv2.waitKey(1)
        if key == ord('e') or key == ord('E'):  # Check if 'e' key is pressed
            break
    cap.release()
    cv2.destroyAllWindows()