import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
#tf = TfidfVectorizer(ngram_range=(1,2), max_features=50000, min_df=1)


# Tách từ
from pyvi import ViTokenizer
class NLP(object):
    def __init__(self, text = None):
        self.text = text

    def segmentation(self):
        return ViTokenizer.tokenize(self.text)

# upload stopword
'''
sw =  open('dataset/stopword.txt')
data_sw = sw.readlines()
data_sw = [x.strip() for x in data_sw]
'''
data_sw = ['là', 'gì']
# hàm loại stopword

def del_stopword(txt):
    t = clean_text(txt)
    if t == '':
        return
    t = NLP(text=t).segmentation()
    t = t.split()
    tt = t
    for x in tt:
      if x in data_sw:
        t.remove(x)
    return t

# Loại bỏ các ký tự đặc biệt
import re, string

def clean_text(text):
  if type(text) != str:
    return
  else:
    text = text.lower()
    text = re.sub('\[.*?]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
  return text
def processing(text):
    text = clean_text(text)
    text = del_stopword(text)
    text = ' '.join(text)
    tf = joblib.load('vocab.pkl')
    text = tf.fit_transform([text])
    return text

text = 'mũi to vl luôn ấy ạ, căng thế nhỉ'


loaded_model = joblib.load('18520194.sav')


text = processing(text)
predict = loaded_model.predict(text)


import gensim
import joblib
from flask import Flask, render_template, request



app = Flask(__name__, template_folder='A:\Download\tdvuit\tdvuit\template')

@app.route('/predict', methods=['GET', 'POST'])
def check():
    if request.method == 'GET':
        return render_template('template.html')
    
    else:
    
        text = request.form['comment']
        text = processing(text)
        prediction = loaded_model.predict(text)
        if (prediction == 0):
            result='Bình luận mang nghĩa thô tục, xúc phạm!'
        if (prediction == 1):
            result='Bình luận bình thường!'
        return render_template('template.html', result_comment=result)
        
 
if __name__ == '__main__':
    app.run(debug=True)