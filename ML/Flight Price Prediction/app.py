import pandas as pd
from flask import Flask, request, render_template
import pickle
import os
import sklearn

app = Flask(__name__)
model = pickle.load(open('flight_price.pkl', 'rb'))


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(
            date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(
            date_dep, format="%Y-%m-%dT%H:%M").month)

        # Departure
        Dep_Hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Dep_Min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_Hour = int(pd.to_datetime(
            date_arr, format="%Y-%m-%dT%H:%M").hour)
        Arrival_Min = int(pd.to_datetime(
            date_arr, format="%Y-%m-%dT%H:%M").minute)

        # Duration
        Duration_Hour = abs(Arrival_Hour - Dep_Hour)
        Duration_Min = abs(Arrival_Min - Dep_Min)

        Total_Duration = (Duration_Hour*60)+Duration_Min

        # Total Stops
        Total_stops = int(request.form["stops"])

        # Airline
        airline = request.form['airline']
        if(airline == 'Air Asia'):
            airline = 0

        elif (airline == 'Air India'):
            airline = 1

        elif (airline == 'GoAir'):
            airline = 2

        elif (airline == 'IndiGo'):
            airline = 3

        elif (airline == 'Jet Airways'):
            airline = 4

        elif (airline == 'Jet Airways Business'):
            airline = 5

        elif (airline == 'Multiple carriers'):
            airline = 6

        elif (airline == 'Multiple carriers Premium economy'):
            airline = 7

        elif (airline == 'SpiceJet'):
            airline = 8

        elif (airline == 'Trujet'):
            airline = 9

        elif (airline == 'Vistara'):
            airline = 10

        elif (airline == 'Vistara Premium economy'):
            airline = 11

        # Source
        Source = request.form["Source"]
        if (Source == 'Banglore'):
            Source = 0

        elif (Source == 'Chennai'):
            Source = 1

        elif (Source == 'Delhi'):
            Source = 2

        elif (Source == 'Kolkata'):
            Source = 3

        elif (Source == 'Mumbai'):
            Source = 4

        # Destination
        Destination = request.form["Destination"]
        if (Destination == 'Banglore'):
            Destination = 0

        elif (Destination == 'Cochin'):
            Destination = 1

        elif (Destination == 'Delhi'):
            Destination = 2

        elif (Destination == 'Hyderabad'):
            Destination = 3

        elif (Destination == 'Kolkata'):
            Destination = 4

        elif (Destination == 'New Delhi'):
            Destination = 5

        prediction = model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_Hour,
            Dep_Min,
            Arrival_Hour,
            Arrival_Min,
            Total_Duration,
            airline,
            Source,
            Destination
        ]])

        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text="Your Flight price is Rs. {}".format(output))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
