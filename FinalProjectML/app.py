import gensim
import joblib
from flask import Flask, render_template, request

from pyvi import ViTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

app = Flask(__name__, template_folder='/template')

class PredictCmt:
  def __init__(self, model_file = 'LSVC.sav'):
    self.model = joblib.load(model_file)
  
  def predict(self, input_cmt):
    X_train = joblib.load('18520194.sav')
    X_train = np.array(X_train)
    lines = input_cmt
   
    title_predict = self.model.predict(lines)
    return title_predict

pt = PredictCmt()
    
@app.route('/')
def ping():
    return 'ok'

@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'GET':
        return render_template('full.html')
    
    else:
    
        title = request.form['title_result']
        prediction = pt.predict(title)
        if (prediction == 0):
            class_title='Bình luận mang nghĩa thô tục, xúc phạm!'
        if (prediction == 1):
            class_title='Bình luận bình thường!'
        return render_template('full.html', class_title=class_title)
        
 
if __name__ == '__main__':
    app.run(debug=True)