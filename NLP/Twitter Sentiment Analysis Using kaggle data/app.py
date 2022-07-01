# import flask libraries
from flask import Flask, render_template, url_for, request
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# load the model from disk
model = pickle.load(open('model.pkl', 'rb'))
# Load count vector from disk
cv = pickle.load(open('transform.pkl', 'rb'))
# Load the vocabulary
words = pickle.load(open('vocabulary.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':
        review = request.form['review']

        data = [review]

        countVect = CountVectorizer(vocabulary=words)
        sentence = countVect.transform(data)

        review_prediction = model.predict(sentence)

        return render_template('result.html', prediction=review_prediction)


if __name__ == '__main__':
    app.run(debug=True)
