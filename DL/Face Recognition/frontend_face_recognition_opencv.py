#importing modules
import cv2
import numpy as np
from keras.preprocessing import image
from PIL import Image
from tensorflow.keras.models import load_model

#importing model and weights
model = load_model('face_recognition_model.h5')
model.load_weights('weights.h5')

#definig the haarcascade face classifier
face_haar_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while cap.isOpened:
    ret, frame = cap.read()
    faces = face_haar_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    if type(frame) is np.ndarray:
        frame = cv2.resize(frame, (224, 224))
        im = Image.fromarray(frame, 'RGB')
        img_array = np.array(im)
        img_array = np.expand_dims(img_array, axis=0)
        pred = model.predict(img_array)
        print(pred)

        if(pred[0][0] > 0.3):
            name = 'Person' #your name here
        cv2.putText(frame, name, (50, 50),
                    cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)

    else:
        cv2.putText(frame, "No Face Found", (50, 50),
                    cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)

    cv2.imshow('image', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #the windwos will close on pressing q
        break

cap.release()
cv2.destroyAllWindows()
