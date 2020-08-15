import gensim
import joblib
from flask import Flask, render_template, request

from pyvi import ViTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

X_train = joblib.load('18520194.sav')
print('a')
