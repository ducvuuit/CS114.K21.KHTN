# Theem cacs thuw vien can thiet
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB

# tai len data
import pandas as pd

data = pd.read_json("Dataset/Sarcasm_Headlines_Dataset_v2.json",lines=True)
X = data['headline']
Y = data['is_sarcastic']
# split test:25%, train:75%
trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.25, random_state=42)

print("[INFO] Used CounterVectorizer ... ")
# su dung phuong phap vector hoa van ban
cv = CountVectorizer()

# chuyen doi tu thanh vecor
trainX = cv.fit_transform(trainX.values).toarray()
trainVocab = cv.vocabulary_
cv = CountVectorizer(vocabulary=trainVocab)
testX = cv.fit_transform(testX.values).toarray()

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB(alpha=2.0, class_prior=None, fit_prior=True)

# train and evaluating
print("   [INFO] evaluating MultinomialBM ... ")
model.fit(trainX, trainY)
predictions = model.predict(testX)
print(classification_report(testY, predictions))
print("\n---------------------------------------\n")

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy' ,random_state=0)

print("   [INFO] evaluating RandomForestClassifier ... ")
model.fit(trainX, trainY)
predictions = model.predict(testX)
print(classification_report(testY, predictions))
print("\n---------------------------------------\n")