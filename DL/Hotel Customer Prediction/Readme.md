# Hotel Customer Prediction

The dataset can be found in the github repo [here.](https://github.com/gurjeet29/Data_Science_Portfolio/tree/main/DL/Hotel%20Customer%20Prediction)

## Project Objective
The purpose of this project is to predict the customers who are going to Check-In in a hotel based on their past records. The project can help hotels to keep track of their customers and improve their services as to avoid cancellation. Booking cancellations have a substantial impact in demand management decisions in the hospitality industry.

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
* Sci-Kit Learn
* Keras
* Tensorflow
* Flask

## Project Description
This project was developed off the data (provided [here](https://github.com/gurjeet29/Data_Science_Portfolio/tree/main/DL/Hotel%20Customer%20Prediction)) which consisted of train and test set in two different csv files with the following features:

* ID : Customer ID
* Nationality : Country of origin
* Age : Customer's age (in years) at the last day of the extraction period
* DaysSinceCreation	:	Number of days since the customer record was created (number of days elapsed between the creation date and the last day of the extraction period)
* AverageLeadTime	: The average number of days elapsed between the customer's booking date and arrival date
* LodgingRevenue : Total amount spent on lodging expenses by the customer (in Euros)
* OtherRevenue : Total amount spent on other expenses by the customer (in Euros)
* BookingsCanceled :	Number of bookings the customer made but subsequently canceled (the costumer informed the hotel he/she would not come to stay)
* BookingsNoShowed : Number of bookings the customer made but subsequently made a “no-show” (did not cancel, but did not check-in to stay at the hotel)
* BookingsCheckedIn : Number of bookings the customer made, and which end up with a staying
* PersonsNights	: The total number of persons/nights that the costumer stayed at the hotel
* RoomNights : Total of room/nights the customer stayed at the hotel (checked-in bookings)
* DaysSinceLastStay : The number of days elapsed between the last day of the extraction and the customer's last arrival date (of a checked-in booking)
* DaysSinceFirstStay : The number of days elapsed between the last day of the extraction and the customer's first arrival date (of a checked-in booking)
* DistributionChannel : Distribution channel usually used by the customer to make bookings at the hotel
* MarketSegment : Current market segment of the customer
* SRHighFloor : Indication if the customer usually asks for a room on a higher floor (0: No, 1: Yes)
* SRLowFloor : Indication if the customer usually asks for a room on a lower floor (0: No, 1: Yes)
* SRAccessibleRoom : Indication if the customer usually asks for an accessible room (0: No, 1: Yes)
* SRMediumFloor : Indication if the customer usually asks for a room on a middle floor (0: No, 1: Yes)
* SRBathtub : Indication if the customer usually asks for a room with a bathtub (0: No, 1: Yes)
* SRShower : Indication if the customer usually asks for a room with a shower (0: No, 1: Yes)
* SRCrib : Indication if the customer usually asks for a crib (0: No, 1: Yes)
* SRKingSizeBed : Indication if the customer usually asks for a room with a king-size bed (0: No, 1: Yes)
* SRTwinBed : Indication if the customer usually asks for a room with a twin bed (0: No, 1: Yes)
* SRNearElevator : Indication if the customer usually asks for a room near the elevator (0: No, 1: Yes)
* SRAwayFromElevator : Indication if the customer usually asks for a room away from the elevator (0: No, 1: Yes)
* SRNoAlcoholInMiniBar : Indication if the customer usually asks for a room with no alcohol in the mini-bar (0: No, 1: Yes)
* SRQuietRoom : Indication if the customer usually asks for a room away from the noise (0: No, 1: Yes)

## Training
A fucntion is created with the follwoing parameters:

```
optimizerL = ['SGD', 'Adam', 'RMSprop', 'Adadelta', 'Adagrad', 'Adamax', 'Nadam', 'Ftrl','SGD']
    
optimizerD= {'Adam':Adam(lr=learning_rate), 'SGD':SGD(lr=learning_rate),
                 'RMSprop':RMSprop(lr=learning_rate), 'Adadelta':Adadelta(lr=learning_rate),
                 'Adagrad':Adagrad(lr=learning_rate), 'Adamax':Adamax(lr=learning_rate),
                 'Nadam':Nadam(lr=learning_rate), 'Ftrl':Ftrl(lr=learning_rate)}

activationL = ['relu', 'sigmoid', 'softplus', 'softsign', 'tanh', 'selu', 'elu', 'exponential', 'LeakyReLU','relu']
```

The range of hyperparameters are set and the Bayesian Optimization is runned:
```
params_nn ={
    'neurons': (10, 100),
    'activation':(0, 9),
    'optimizer':(0,7),
    'learning_rate':(0.01, 1),
    'batch_size':(200, 1000),
    'epochs':(20, 100)
}

nn_bo = BayesianOptimization(nn_cl_bo, params_nn, random_state=111)
nn_bo.maximize(init_points=25, n_iter=4)
```

The model is fined tuned and runned to get the best hyperparameters for the final training:
```
params_nn2 ={
    'neurons': (10, 100),
    'activation':(0, 9),
    'optimizer':(0,7),
    'learning_rate':(0.01, 1),
    'batch_size':(200, 1000),
    'epochs':(20, 100),
    'layers1':(1,3),
    'layers2':(1,3),
    'normalization':(0,1),
    'dropout':(0,1),
    'dropout_rate':(0,0.3)
}

nn_bo = BayesianOptimization(nn_cl_bo2, params_nn2, random_state=111)
nn_bo.maximize(init_points=25, n_iter=4)
```

Training the Neural Network with the best tuned parameters:
```
model = Sequential()
model.add(Dense(params_nn_['neurons'], input_dim=X_train.shape[1], activation=params_nn_['activation']))

if params_nn_['normalization'] > 0.5:
  model.add(BatchNormalization())

for i in range(params_nn_['layers1']):
  model.add(Dense(params_nn_['neurons'], activation=params_nn_['activation']))

if params_nn_['dropout'] > 0.5:
  model.add(Dropout(params_nn_['dropout_rate'], seed=123))

for i in range(params_nn_['layers2']):
  model.add(Dense(params_nn_['neurons'], activation=params_nn_['activation']))

model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer=params_nn_['optimizer'], metrics=['accuracy'])
model.summary()
        
es = EarlyStopping(monitor='accuracy', mode='max', verbose=0, patience=20)
```
The output layer consist of `1` neuron with activation function `sigmoid` and loss `binary_crossentropy`. After tharing the model the best max value obtained for accuracy wad `97.4%` and the best max value obtained for validation accuracy was `97.6%`.

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
