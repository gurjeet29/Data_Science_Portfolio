# Face Recognition

## Project Objective
This project is a basic face recognizer application which can identify the face(s) of the person(s) showing on a web cam.

## Methods Used
* Inferential Statistics
* Deep Learning
* Convolutional Neural Networks

## Technologies
* Python
* Pandas
* Jupyter
* Matplotlib
* Numpy
* Sci-Kit Learn (for data handling)
* Keras
* Tensorflow
* OpenCV
* Flask

## Project Description
Its a basic face recognizer application which can identify the face(s) of the person(s) showing on a web cam. The implementation is inspired by two path breaking papers on facial recognition using deep convoluted neural network, namely FaceNet and DeepFace. I have used the pre-trained model VGG19 to train the model on my own collected dataset.

## One Shot Learning
In one shot learning, only one image per person is stored in the database which is passed through the neural network to generate an embedding vector. This embedding vector is compared with the vector generated for the person who has to be recognized. If there exist similarities between the two vectors then the system recognizes that person, else that person is not there in the database. This can be understood by below picture.

![oneshot](https://user-images.githubusercontent.com/84326897/180245540-293072d8-15f6-41b4-a4f9-3b0d66432e0c.jpg)

## Collecting Images
The file `collecting_images.py` collects images captured from a webcam and store them in different directories to generate dataset. Based on the key pressed by the user the images are captured by OpenCV and stored in directory of the user name under train and test folder.

```python
train_path = os.path.join('Dataset', 'train', 'person')
test_path = os.path.join('Dataset', 'test', 'person')
```
In the above code replace person with your own name or any other person's name you want to capture images. This will create a training and testing data set of that person.
Example:

```python
train_path = os.path.join('Dataset', 'train', 'Mark')
test_path = os.path.join('Dataset', 'test', 'Mark')
```
To capture images:

```python
# on pressing a the images will be captured and stored on the train path
    if cv2.waitKey(1) & 0xFF == ord('a'):
        imgname = os.path.join(train_path, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgname, frame)

    # on pressing p the images will be captured and stored on the test path
    if cv2.waitKey(1) & 0xFF == ord('p'):
        imgname = os.path.join(test_path, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgname, frame)
```
On pressing `a` the images will be captured and stored on the train path and on pressing `p` the images will be captured and stored on the test path.

**IF YOU FIND ANY ISSUES OR BUGS PLEASE OPEN AN ISSUE**
