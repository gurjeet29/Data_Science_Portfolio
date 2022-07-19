# Butterfly Species Classification

The dataset can be found in this link: [dataset](https://www.kaggle.com/datasets/gpiosenka/butterfly-images40-species)

## Project Objective
The purpose of this project is to classify between different species of butterflies based of a picture of a butterfly. Butterflies are important and crucial to our ecosystem. They are vital in pollination, as they spread pollen when they collected nectar, and the ability to classify between them would lead to knowing which butterflies are more useful in pollination. 

## Methods Used
* Inferential Statistics
* Deep Learning
* Convolutional Neural Networks

## Technologies
* Python
* Pandas
* Jupyter & Matplotlib
* Numpy
* Sci-Kit Learn (for data handling)
* Keras & Tensorflow
* Flask
* Tkinter

## Project Description
This project was developed off the data (provided [here](https://www.kaggle.com/datasets/gpiosenka/butterfly-images40-species)) which consisted
of different images of butterflies. The data is divided innto 3 different folders: train, valid and test.

## Training
**Using pre-trained weights of EfficientNetB7**   

In this method a pre-trained EfficientNetB7 network was taken from pre-trained model zoo, a output classifier for butterfly species was connected to the last fully connected layer of the EfficientNetB7 network, so that we can get probabilities/score for 75 categories(butterfly species). After that network was trained for 30 epochs. This model gave best validation accuracy of 85% and training accuracy of 95%.

The model and the pre-trained weights are saved in an **h5** file. Saving the model there would allow us to make predictions quicker.

## Testing
Testing the model to check the accuracy of the model.

![Output](https://user-images.githubusercontent.com/84326897/179824138-f17cf8d7-f19f-4704-91a4-591af85dcb80.png)

## GUI
The file `gui.py` shows a GUI for the same model which can be run locally. On uploading an image the output is shown on the GUI.
![Output](https://user-images.githubusercontent.com/84326897/179828761-d178920e-d80d-4504-9d63-0bebb8fbdbec.png)


## Achievement
What this project was designed for was to mainly test my knowledge about deep learning and whether or not I can make a reliable model based off a dataset. Instead of tackling the MNIST sets, I wanted to do something different but just as similar. Typical MNIST dataset tutorials give you a preprocessed dataset all in one line of
code. Where's the fun in that? Where's the data pre-processing? I opted for doing all that by myself and it seemed to work in my favor.


**IF YOU FIND ANY ISSUES OR BUGS PLEASE OPEN AN ISSUE**
