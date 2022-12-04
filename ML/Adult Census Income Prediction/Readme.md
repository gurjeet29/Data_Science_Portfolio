# Adult Census Income Prediction

The dataset can be found [here.](https://www.kaggle.com/overload10/adult-census-dataset)

**The deployed model can be found on this link: https://income-predictor-1.herokuapp.com/**

## Project Objective
The Goal is to predict whether a person has an income of more than 50K a year or not. This is basically a binary classification problem where a person is classified into the >50K group or <=50K group.

## Technical Aspects
The whole project has been divided into three parts. These are listed as follows :

* Data Preparation : This consists of storing our data into cassandra database and utilizing it, Data Cleaning, Feature Engineering, Feature Selection, EDA, etc.
* Model Development : In this step, we use the resultant data after the implementation of the previous step to cross validate our Machine Learning model and perform Hyperparameter optimization based on various performance metrics in order to make our model predict as accurate results as possible.
* Model Deployment : This step include creation of a front-end using Flask and Heroku to put our trained model into production.

## Technologies
* Python
* Pandas
* Jupyter
* Matplotlib
* Numpy
* Sci-Kit Learn
* Flask

## Installation
The Code is written in Python 3.10. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:
```
pip install -r requirements.txt
```

## Run on your Local Machine
To run the flask server on your local machine, first navigate to your folder conatining the project and then just run the following code in your command prompt in the project directory:
```
python app.py
```

## Project Description
The dataset contains 15 columns and 32000+ rows with the following features:

* age : the age of an individual (Integer greater than 0 )
* workclass : a general term to represent the employment status of an individual
* fnlwgt: final weight. In other words, this is the number of people the census believes the entry represents.(Integer greater than 0)
* education: the highest level of education achieved by an individual.
* education-num: the highest level of education achieved in numerical form.(Integer greater than 0)
* marital-status: marital status of an individual.
* occupation: the general type of occupation of an individual
* relationship: represents what this individual is relative to others. For example an individual could be a Husband. Each entry only has one relationship attribute and is somewhat redundant with marital status.
* race: Descriptions of an individual’s race
* sex: the biological sex of the individual
* capital-gain: capital gains for an individual (Integer greater than or equal to 0)
* capital-loss: capital loss for an individual (Integer greater than or equal to 0)
* hours-per-week: the hours an individual has reported to work per week continuous.
* native­country: country of origin for an individual
* salary: whether or not an individual makes more than $50,000 annually.

## Training
We have used different ML classification Algorithms to train the model.

```
models = [['LogisticRegression : ', LogisticRegression()],
          ['DecisionTreeClassifier : ', DecisionTreeClassifier()],
          ['RandomForestClassifier : ', RandomForestClassifier()],
          ['AdaBoostClassifier : ', AdaBoostClassifier()],
          ['SVC : ', SVC()],
          ['KNeighborsClassifier : ', KNeighborsClassifier()],
          ['GaussianNB : ', GaussianNB()],
          ['CatBoostClassifier : ', CatBoostClassifier()],
          ['XGBClassifier : ', XGBClassifier()]]
```
The model is evaluated on basis of ```F1 score```.

The model is saved in a pickle file. Saving the model there would allow us to make predictions quicker.

## Deployment
The model created using the Flask's Rest API and is deployed using heroku to do real time predictions:

**Deployed model link: https://income-predictor-1.herokuapp.com/**

![image](https://user-images.githubusercontent.com/84326897/201537270-1a25bb6d-a1e7-4589-a3f0-bbef4771a5ec.png)

![image](https://user-images.githubusercontent.com/84326897/201537293-89485589-2d9c-48d8-81ba-8ac628f90e9e.png)

## Achievement
This end-to-end project is made as a part of data science internship for [Ineuron.ai](https://ineuron.ai/).

## Appendix
Link for youtube video regarding description of the project:
https://youtu.be/nAkT4fTuu8w

## Author
[Gurjeet Singh](https://github.com/gurjeet29/)

## License
[MIT](https://choosealicense.com/licenses/mit/)

Copyright 2022 Gurjeet Singh

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Bugs
**IF YOU FIND ANY ISSUES OR BUGS PLEASE OPEN AN ISSUE**
