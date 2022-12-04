from flask import Flask, request, render_template
from flask_material import Material
import pandas as pd
import pickle


dct = {'Preschool': 1.0, '1st-4th': 2.0, '5th-6th': 3.0, '7th-8th': 4.0, '9th': 5.0, '10th': 6.0, '11th': 7.0, '12th': 8.0, 'HS-grad': 9.0,
       'Some-college': 10.0, 'Assoc-voc': 11.0, 'Assoc-acdm': 12.0, 'Bachelors': 13.0, 'Masters': 14.0, 'Prof-school': 15.0, 'Doctorate': 16.0}

app = Flask(__name__)
Material(app)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        home_page = "home"
        return render_template('index.html', home_page=home_page)
    except Exception as e:
        return str(e)


@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':

        age = int(request.form['age'])

        marital_status = request.form['marital_status']
        if (marital_status == 'Single'):
            marital_status = 0
        else:
            marital_status = 1

        sex = request.form['sex']
        if (sex == 'Male'):
            sex = 1
        else:
            sex = 0

        education = request.form['education']
        education = dct[education]

        hours_per_week = int(request.form['hours_per_week'])

        gain_or_loss = int(request.form['gain_or_loss'])

        country = request.form['country']
        if (country == 'US'):
            country = 1
        else:
            country = 0

        employment_type = request.form['employment_type']
        if (employment_type == 'Private'):
            employment_type = 1

        elif (employment_type == 'Government'):
            employment_type = 2

        elif (employment_type == 'Self-Employed'):
            employment_type = 3

        elif (employment_type == 'Unemployed'):
            employment_type = 4

        occupation = request.form['occupation']
        if (occupation == 'Adm clerical'):
            occupation = 0
        elif (occupation == 'Armed Forces'):
            occupation = 1
        elif (occupation == 'Craft repair'):
            occupation = 2
        elif (occupation == 'Exec managerial'):
            occupation = 3
        elif (occupation == 'Farming fishing'):
            occupation = 4
        elif (occupation == 'Handlers cleaners'):
            occupation = 5
        elif (occupation == 'Machine op inspct'):
            occupation = 6
        elif (occupation == 'Other service'):
            occupation = 7
        elif (occupation == 'Priv house serv'):
            occupation = 8
        elif (occupation == 'Prof specialty'):
            occupation = 9
        elif (occupation == 'Protective serv'):
            occupation = 10
        elif (occupation == 'Sales'):
            occupation = 11
        elif (occupation == 'Tech support'):
            occupation = 12
        elif (occupation == 'Transport moving'):
            occupation = 13

        data = {
            'age': age,
            'marital_status': marital_status,
            'sex': sex,
            'education': education,
            'hours_per_week': hours_per_week,
            'gain_or_loss': gain_or_loss,
            'country': country,
            'employment_type': employment_type,
            'occupation': occupation}

    df_predict = pd.DataFrame(data=data, index=[1])

    prediction = model.predict(df_predict)

    if prediction[0] == 1:
        prediction = "The Income is greater than 50K$"
    else:
        prediction = "The Income is less than 50K$"

    return render_template('index.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
