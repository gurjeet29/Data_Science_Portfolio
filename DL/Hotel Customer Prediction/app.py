from flask import Flask, render_template, request
from flask_material import Material
from keras.models import load_model
import pandas as pd

model = load_model('hotel_customer_model.h5')
model.load_weights('weights.h5')


app = Flask(__name__)
Material(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        Age = request.form['Age']
        AverageLeadTime = request.form['AverageLeadTime']
        MarketSegment = request.form['MarketSegment']
        DistributionChannel = request.form['DistributionChannel']
        SRHighFloor = request.form['SRHighFloor']
        SRBathtub = request.form['SRBathtub']
        SRCrib = request.form['SRCrib']
        SRKingSizeBed = request.form['SRKingSizeBed']
        SRTwinBed = request.form['SRTwinBed']
        SRNearElevator = request.form['SRNearElevator']
        SRNoAlcoholInMiniBar = request.form['SRNoAlcoholInMiniBar']
        SRQuietRoom = request.form['SRQuietRoom']
        total_revenue = request.form['total_revenue']
        PersonsperRoom = request.form['PersonsperRoom']

        Age = int(Age)
        AverageLeadTime = int(AverageLeadTime)
        MarketSegment = int(MarketSegment)
        DistributionChannel = int(DistributionChannel)
        SRHighFloor = int(SRHighFloor)
        SRBathtub = int(SRBathtub)
        SRCrib = int(SRCrib)
        SRKingSizeBed = int(SRKingSizeBed)
        SRTwinBed = int(SRTwinBed)
        SRNearElevator = int(SRNearElevator)
        SRNoAlcoholInMiniBar = int(SRNoAlcoholInMiniBar)
        SRQuietRoom = int(SRQuietRoom)
        total_revenue = float(total_revenue)
        PersonsperRoom = int(PersonsperRoom)

        data = {
            'Age': Age,
            'AverageLeadTime': AverageLeadTime,
            'MarketSegment': MarketSegment,
            'DistributionChannel': DistributionChannel,
            'SRHighFloor': SRHighFloor,
            'SRBathtub': SRBathtub,
            'SRCrib': SRCrib,
            'SRKingSizeBed': SRKingSizeBed,
            'SRTwinBed': SRTwinBed,
            'SRNearElevator': SRNearElevator,
            'SRNoAlcoholInMiniBar': SRNoAlcoholInMiniBar,
            'SRQuietRoom': SRQuietRoom,
            'total_revenue': total_revenue,
            'PersonsperRoom': PersonsperRoom}

    df_predict = pd.DataFrame(data=data, index=[1])

    prediction = model.predict(df_predict)
    can_prediction=round(100 * prediction[0][0],2)
    print(f'The Chances of cancellation is {round(100 * prediction[0][0],2)}%')

    final_prediction = ""

    if prediction[0] > 0.5:
        final_prediction = "not Check In"

    else:
        final_prediction = "Check In"

    return render_template('index.html', Age=Age,
                           AverageLeadTime=AverageLeadTime,
                           MarketSegment=MarketSegment,
                           DistributionChannel=DistributionChannel,
                           SRHighFloor=SRHighFloor,
                           SRBathtub=SRBathtub,
                           SRCrib=SRCrib,
                           SRKingSizeBed=SRKingSizeBed,
                           SRTwinBed=SRTwinBed,
                           SRNearElevator=SRNearElevator,
                           SRNoAlcoholInMiniBar=SRNoAlcoholInMiniBar,
                           SRQuietRoom=SRQuietRoom,
                           total_revenue=total_revenue,
                           PersonsperRoom=PersonsperRoom,
                           prediction=prediction,
                           can_prediction=can_prediction,
                           final_prediction=final_prediction)


if __name__ == '__main__':
    app.run(debug=True)
