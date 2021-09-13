from flask import Flask, escape, request, render_template
import pickle

import numpy as np


app = Flask(__name__)
model = pickle.load(open('wqi.pkl','rb'))

@app.route('/')
def home():
    return render_template("web.html")

@app.route('/predict',methods = ['GET','POST'])
def predict():

    if request.method == "POST":
            year = request.form["year"]
    do = request.form["do"]
    ph = request.form["ph"]
    nco = request.form["nco"]
    bod = request.form["bod"]
    na = request.form["na"]
    tc = request.form["tc"]
    total = [[int(year),float(do),float(ph),float(nco),float(bod),float(na),float(tc)]]
    y_pred = model.predict(total)
    print(y_pred)
    y_pred =y_pred[[0]]
    if(y_pred >= 95 and y_pred <= 100) :
        return render_template("web.html",showcase = 'Excellent,The predicted value is '+ str(y_pred))
    elif(y_pred >= 89 and y_pred <= 94) :
        return render_template("web.html",showcase = 'Very good,The predicted value is '+str(y_pred))
    elif(y_pred >= 80 and y_pred <= 88) :
        return render_template("web.html",showcase = 'Good,The predicted value is'+str(y_pred))
    elif(y_pred >= 65 and y_pred <= 79) :
        return render_template("web.html",showcase = 'Fair,The predicted value is '+str(y_pred))
    elif(y_pred >= 45 and y_pred <= 64) :
        return render_template("web.html",showcase = 'Marginal,The predicted value is '+str(y_pred))
    else :
        return render_template("web.html",showcase = 'Poor,The predicted value is '+str(y_pred))


    
    
if __name__ == "__main__":
    app.run(debug=True)
