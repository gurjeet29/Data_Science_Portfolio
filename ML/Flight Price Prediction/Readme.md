# Flight Price Prediction

## Project Objective
Nowadays flight prices are quite unpredictable. The ticket prices change frequently. Customers are seeking to get the lowest price for their tickets, while airline companies are trying to keep their overall revenue as high as possible. Using technology it is actually possible to reduce the uncertainty of flight prices. The purpose of this project is to predict the flight prices using efficient machine learning techniques.

## Methods Used
* Inferential Statistics
* Machcine Learning
* EDA
* Feature engineering
* Feature Selection

## Technologies
* Python
* Pandas
* Jupyter
* Matplotlib
* Numpy
* Sci-Kit Learn (for data handling)
* Flask

## Dataset Description
We will be using two datasets, train data, and test data. The train data comprises 10683 rows and 11 attributes whereas the test data has 2671 rows. The dataset conatins the following features:

 - Airline: This column will have all the different types of airlines like Indigo, Jet Airways, Air India, and many more.
 - Date_of_Journey: This column will let us know the date on which the passenger’s journey will start.
 - Source: This column holds the name of the place from where the passenger’s journey will start.
 - Destination: This column holds the name of the place to which passengers wanted to travel.
 - Route: Here we can know about that what is the route through which passengers have opted to travel from their source to their destination.
 - Arrival_Time: Arrival time is when the passenger will reach his/her destination.
 - Duration: Duration is the whole period that a flight will take to complete its journey from source to destination.
 - Total_Stops: This will let us know how many places flights will stop there for the flight in the whole journey.
 - Additional_Info: In this column, we will get information about food, the kind of food, and other amenities.
 - Price: Price of the flight for a complete journey including all the expenses before onboarding.

## Training 
We have used different ML regression Algorithms to train the model.

```python
models = [['LinearRegression : ', LinearRegression()],
          ['ElasticNet :', ElasticNet()],
          ['Lasso : ', Lasso()],
          ['Ridge : ', Ridge()],
          ['KNeighborsRegressor : ', KNeighborsRegressor()],
          ['DecisionTreeRegressor : ', DecisionTreeRegressor()],
          ['RandomForestRegressor : ', RandomForestRegressor()],
          ['SVR : ', SVR()],
          ['AdaBoostRegressor : ', AdaBoostRegressor()],
          ['GradientBoostingRegressor : ', GradientBoostingRegressor()],
          ['ExtraTreeRegressor : ', ExtraTreeRegressor()],
          ['HuberRegressor : ', HuberRegressor()],
          ['BayesianRidge : ', BayesianRidge()]]
```

The model is evaluated on basis of `Root mean square error (RMSE)` and the accuarcy is checked by `r2 score`.

The model is saved in a pickle file. Saving the model there would allow us to make predictions quicker.

## Testing
Testing the model to check the accuracy of the model.



## Deployment
The model is deployed on Heroku to do real-time prediction. You can find the deployed model on this link: https://flight-price-predict0.herokuapp.com/

![deploy](https://user-images.githubusercontent.com/84326897/180394984-642b7a23-4612-467b-adcb-b5b0aac32f93.png)

## Achievement
What this project was designed for was to mainly test my knowledge about machine learning and whether or not I can make a reliable model based off a dataset. Instead of tackling the basic sets, I wanted to do something different but just as similar and it seemed to work in my favor.

**IF YOU FIND ANY ISSUES OR BUGS PLEASE OPEN AN ISSUE**
