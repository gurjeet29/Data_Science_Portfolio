# -*- coding: utf-8 -*-
"""Fake_News_Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yw_gYM9TkzQ9m4rFnTcBQJYCcP4wlgQ5
"""

!nvidia-smi -L

# Commented out IPython magic to ensure Python compatibility.
#importing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

#reading csv file
df=pd.read_csv('/content/train.csv')
df.head()

#dropping unnecessary coulmns
df.drop(['id','title','author'],axis=1,inplace=True)
df.head()

#checking null values 
df.isnull().sum()

#droppping null values
df=df.dropna()

#resetting index
df.reset_index(inplace=True)

#spliiting into columns and features
X=df.drop('label',axis=1)
y=df['label']

#dropping index
X.drop(['index'],axis=1,inplace=True)

X.shape, y.shape

#checking distribution of label
y.value_counts()

from tensorflow.keras.layers import Dense, LSTM, Bidirectional, Dropout, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.models import Sequential

voc_size=5000
import nltk
import re
nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
corpus = []
for i in range(0, len(X)):
    review = re.sub('[^a-zA-Z]', ' ', X['text'][i])
    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)

#converting words to one hot representation
onehot_repr=[one_hot(words,voc_size)for words in corpus] 
onehot_repr

#adding padding to sentences
sent_length=20
embedded_docs=pad_sequences(onehot_repr,padding='pre',maxlen=sent_length)
print(embedded_docs)

## Creating model
embedding_vector_features=40
model=Sequential()
model.add(Embedding(voc_size,embedding_vector_features,input_length=sent_length))
model.add(Bidirectional(LSTM(100)))
model.add(Dropout(0.3))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
print(model.summary())

len(embedded_docs),y.shape

#converting to array
X_final=np.array(embedded_docs)
y_final=np.array(y)

X_final.shape,y_final.shape

#splitting data into train and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_final, y_final, test_size=0.20, random_state=42)

#Training the model
hist=model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=30,batch_size=64).history

#checking the max and min value
training_features1= ['accuracy', 'val_accuracy']
training_features2= ['loss', 'val_loss']
for feature in training_features1:   
    print("The best max value obtained for {} is :".format(feature),max(hist[feature]))

for feature in training_features2:   
    print("The best min value obtained for {} is :".format(feature),min(hist[feature]))

#plotting loss vs val_loss and acc vs val_acc
acc = hist['accuracy']
val_acc = hist['val_accuracy']
epochs = range(len(acc))

plt.plot(epochs, acc, 'b', label='Training Accuracy')
plt.plot(epochs, val_acc, 'r', label='Validation Accuracy')
plt.title('Accuracy Graph')
plt.legend()
plt.figure()

loss = hist['loss']
val_loss = hist['val_loss']
plt.plot(epochs, loss, 'b', label='Training Loss')
plt.plot(epochs, val_loss, 'r', label='Validation Loss')
plt.title('Loss Graph')
plt.legend()
plt.show()

y_pred = (model.predict(X_test) > 0.5).astype("int32")

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report

#plotting confusion matrix
confusion_matrix(y_test,y_pred)

#checking accuracy score
accuracy_score(y_test,y_pred)

#checking classification report
print(classification_report(y_test,y_pred))

#saving model
model.save('fake_news_classification.h5')
#saving weights
model.save_weights('weights.h5')

#custom testing
def new_review(new_review):
    ps = PorterStemmer()
  
    new_review = new_review
    new_review = re.sub('[^a-zA-Z]', ' ', new_review)
    new_review = new_review.lower()
    new_review = new_review.split()

    new_review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    new_review = ' '.join(new_review)
    new_corpus = [new_review]

    onehot_repr = [one_hot(words,voc_size)for words in new_corpus]
    embedded_docs = pad_sequences(onehot_repr,padding='pre',maxlen=sent_length)

    new_X_test = np.array(embedded_docs)
    new_y_pred = model.predict(new_X_test)
    return new_y_pred

new_review = new_review(str(input("Enter new review...")))
new_review

pred = (new_review > 0.5).astype("int32")
if pred[0]==1:
    print("This news is FAKE!!")
else:
    print("This news is TRUE!!")

