from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

import numpy as np 
import pandas as pd 
import re,string
'''
def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text
'''
data_train = pd.read_json("Dataset/Sarcasm_Headlines_Dataset-v2.json")

X = data_train['headline']
Y = data_train['is_sarcastic']
'''
#split validation:25%, train:75%
trainX,valX,trainY,valY = train_test_split(X,Y,test_size=0.25,random_state=42)

onion = pd.read_json("Dataset/new_onion_headlines.json")
onion_X = onion['headline']
onion_Y = onion['is_sarcastic']

huffpost = pd.read_json("Dataset/new_huffpost_headlines.json")
huffpost_X = huffpost['headline']
huffpost_Y = huffpost['is_sarcastic']

trainX = trainX.apply(clean_text)

valX = valX.apply(clean_text)
onion_X = onion_X.apply(clean_text)
huffpost_X = huffpost_X.apply(clean_text)


# khởi tạo TfidfVectorizer
tf = TfidfVectorizer(ngram_range=(1,2), max_features=40000, min_df=2)

# chuyển words sang vetor
trainX = tf.fit_transform(trainX.values).toarray()
trainVocab = tf.vocabulary_ 
tf = TfidfVectorizer(vocabulary=trainVocab)

valX = tf.fit_transform(valX.values).toarray()

onion_X = tf.fit_transform(onion_X.values).toarray()
huffpost_X = tf.fit_transform(huffpost_X.values).toarray()
testX = np.concatenate((onion_X,huffpost_X),axis=0)
testY = np.concatenate((onion_Y,huffpost_Y),axis=0)
print("[INFO] Used TfidfVectorizer ... ")


model1 = LogisticRegression()
model2 = MultinomialNB()
model3 = LinearSVC()

for i in range(3):
    
    if i == 0:

        print("   [INFO] evaluating Logistic Regression...")

        # train and evaluating 
        model1.fit(trainX, trainY)
        predict_val_1 = model1.predict(valX)
        predict_test_1 = model1.predict(testX)

        print(classification_report(valY,predict_val_1))

    if i == 1:
        
        print("   [INFO] evaluating Naive Bayes...")

        # train and evaluating 
        model2.fit(trainX, trainY)
        predict_val_2 = model2.predict(valX)
        predict_test_2 = model2.predict(testX)

        print(classification_report(valY,predict_val_2))

    if i == 2:

        print("   [INFO] evaluating SVM...")

        model3.fit(trainX, trainY)
        predict_val_3 = model3.predict(valX)
        predict_test_3 = model3.predict(testX)

        print(classification_report(valY,predict_val_3))
'''