from datetime import time
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('modelRF.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    age_form = request.form['age'].value
    creatinine_phosphokinase_form = request.form['creatinine_phosphokinase'].value
    ejection_fraction_form = request.form['ejection_fraction'].value
    serum_creatinine_form = request.form['serum_creatinine'].value
    time_form = request.form['time'].value
    status_form = ""

    result = ""
    if prediction == 1:
      status_form = "Meninggal"
      result = 'Berdasarkan record tersebut, orang yang bersangkutan sudah meninggal'
    else:
      status_form = "Hidup"
      result = 'Berdasarkan record tersebut, orang yang bersangkutan tidak meninggal'

    return render_template('index.html', prediction_text='{}'.format(result), age='{}'.format(age_form), creatinine_phosphokinase='{}'.format(creatinine_phosphokinase_form), ejection_fraction='{}'.format(ejection_fraction_form), serum_creatinine='{}'.format(serum_creatinine_form), time='{}'.format(time_form), status='{}'.format(status_form))


if __name__ == "__main__":
    app.run(debug=True)