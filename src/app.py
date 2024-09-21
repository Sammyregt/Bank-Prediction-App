from flask import Flask, render_template, request
#from sklearn.externals import joblib
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

#@app.route('/test')
#def test():
#    return "Flask is being used for development"

ml_open = open('finalized_model.pkl', 'rb')
ml_model = pickle.load(ml_open)
#ml_model = joblib.load(mul_reg)

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    '''
    CustomerSince
    HighestSpend
    HiddenScore
    MonthlyAverageSpend
    Level
    Montage
    Security
    FixedDepositAccount
    InternetBanking
    CreditCard
    '''

    if request.method == 'POST':
        print(request.form.get('CustomerSince'))
        try:
            CustomerSince = int(request.form["CustomerSince"])
            HighestSpend = float(request.form["HighestSpend"])
            HiddenScore	 = int(request.form["HiddenScore"])
            MonthlyAverageSpend = float(request.form["MonthlyAverageSpend"])
            Level = int(request.form["Level"])
            Montage = float(request.form["Montage"])
            Security = float(request.form["Security"])
            FixedDepositAccount = int(request.form["FixedDepositAccount"])
            InternetBanking = int(request.form["InternetBanking"])
            CreditCard = int(request.form["CreditCard"])

            pred_args = [CustomerSince, HighestSpend, HiddenScore, MonthlyAverageSpend, 
                         Level, Montage, Security, FixedDepositAccount, InternetBanking, CreditCard]
            
            pred_args_arr = np.array(pred_args)

            pred_args_arr = pred_args_arr.reshape(1, -1)
            print(pred_args_arr)
            #ml_open = open('finalized_model.pkl', 'rb')
            #ml_model = pickle.load(ml_open)
            model_prediction = ml_model.predict(pred_args_arr)
            print(model_prediction)

        except ValueError:
            return "Please check if the values are entered correctly"
    return render_template('predict.html', prediction = model_prediction)


if __name__ == "__main__":
    app.run(host="0.0.0.0")