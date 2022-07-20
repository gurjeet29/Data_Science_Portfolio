# Customer Churn Prediction

The dataset can be found in this link: [dataset](https://www.kaggle.com/code/kmalit/bank-customer-churn-prediction)

## Project Objective
The purpose of this project is to predict which customers are likely to leave a service or to cancel a subscription to a service. It is a critical prediction for many businesses because acquiring new clients often costs more than retaining existing ones.

## Methods Used
* Inferential Statistics
* Deep Learning
* Artificial Neural Networks

## Technologies
* Python
* Pandas
* Jupyter
* Matplotlib
* Numpy
* Sci-Kit Learn (for data handling)
* Keras & Tensorflow

## Project Description
The dataset `Churn_Modelling.csv` contains records of 10,000 customers of bank with following columns:

- RowNumber
- CustomerId
- Surname
- CreditScore
- Geography
- Gender
- Age
- Tenure
- Balance
- NumOfProducts
- HasCrCard
- IsActiveMember
- EstimatedSalary
- Exited

By using all the the features we have to predict whether the user will exit the bank or not.

## Training
**Simple ANN Model using Keras**   

- Create ANN with total 4 layers:
    - One input layer with 11 input features and 6 output features
    - Hidden layer with 6 output features
    - Final layer with 1 output feature

- Activation Functions
    - 1st layer: Relu
    - 2nd layer: Relu
    - 3rd layer: Sigmoid

- Hyperparameters
    - optimizer: `'adam'`
    - loss: `'binary_crossentropy'`
    - metrics: `'accuracy'`
    - batch_size: `32`
    - epochs: `100`

- Accuracy(Subject to change)
    - Training Set: 0.86
    - Testing Set: 0.85

## Further Improvements
We can further imporve the model by changing hyperparameters and trying other range of values using GridSearchCV. But it is important to note that, as we will increase number of parameters in GridSearchCV, our time for training will also increase.

## Achievement
This project was designed to mainly test my knowledge about deep learning and whether or not I can make a reliable model based off a simple dataset.

**IF YOU FIND ANY ISSUES OR BUGS PLEASE OPEN AN ISSUE**
