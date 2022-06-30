import cv2
import os
import uuid

# replace person with your own name below and then other person name name to create a dataset of binary classification

train_path = os.path.join('Dataset', 'train', 'person')
test_path = os.path.join('Dataset', 'test', 'person')

face_haar_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while cap.isOpened():
    ret, frame = cap.read()

    # on pressing a the images will be captured and stored on the train path
    if cv2.waitKey(1) & 0xFF == ord('a'):
        imgname = os.path.join(train_path, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgname, frame)

    # on pressing p the images will be captured and stored on the test path
    if cv2.waitKey(1) & 0xFF == ord('p'):
        imgname = os.path.join(test_path, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgname, frame)

    cv2.imshow('images', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # the window will close on pressing q
        break

cap.release()
cv2.destroyAllWindows()
