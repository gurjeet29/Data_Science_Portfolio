# Face Emotion Recognition

The dataset can be found in this link: [dataset](https://www.kaggle.com/datasets/deadskull7/fer2013)

![EmotionRecognitionOutput](https://user-images.githubusercontent.com/84326897/180078275-0094a9e8-1ca4-440a-b121-37872452922a.gif)

## Project Objective
This project aims to classify the emotion on a person's face into one of seven categories, using deep convolutional neural networks. The model is trained on the FER-2013 dataset which was published on International Conference on Machine Learning (ICML).

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
This project was developed off the data (provided [here](https://www.kaggle.com/datasets/deadskull7/fer2013)) which consisted of face emotions and their pixels in a csv file. There are seven emotions in the dataset- angry, disgusted, fearful, happy, neutral, sad and surprised.

## Training
**Custom CNN Model**   

- Create CNN with a total of 5 block and following layers:
    - Conv2D
    - BatchNormalization
    - MaxPooling2D
    - Dropout
    - Dense

- Activation Functions
    - Hidden layers: Relu
    - Output layer: Softmax

    - Padding: Same

- Hyperparameters
    - optimizer: adam
    - learning_rate: 0.0001
    - decay: 1e-6
    - loss: categorical_crossentropy
    - metrics: accuracy
    - batch_size: 64
    - epochs: 100

- Accuracy(Subject to change)
    - Training Set: 0.88
    - Testing Set: 0.69

- Plot
  
  ![image](https://user-images.githubusercontent.com/84326897/180083273-2859bc28-85bc-43f9-9304-cb06de014486.png)

## Testing
Testing the model to check the accuracy of the model.



## Achievement
This project was designed for was to mainly test my knowledge about deep learning and whether or not I can make a reliable model based off a dataset. Instead of tackling the MNIST sets, I wanted to do something different but just as similar. Typical MNIST dataset tutorials give you a preprocessed dataset all in one line of
code. Where's the fun in that? Where's the data pre-processing? I opted for doing all that by myself and it seemed to work in my favor.


**IF YOU FIND ANY ISSUES OR BUGS PLEASE OPEN AN ISSUE**
