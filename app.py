from flask import Flask,render_template,request

from Feature_Extractor import extract_features
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/getURL',methods=['GET','POST'])
def getURL():
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        data = extract_features(url)
        print(data)
        DTmodel = pickle.load(open('./models/DTClassifier.pickle.dat', 'rb'))
        predicted_value = DTmodel.predict(np.array(data).reshape(1, -1))
        #print(predicted_value)
        if predicted_value == 0:    
            value = "The URL seems fine"
            return render_template("home.html",error=value)
        else:
            value = "The URL might be a phishing link"
            return render_template("home.html",error=value)
if __name__ == "__main__":
    app.run(debug=True)