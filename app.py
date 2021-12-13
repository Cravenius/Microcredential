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

    data = {}
    data['age'] = request.form['age'].value
    data['creatinine_phosphokinase'] = request.form['creatinine_phosphokinase'].value
    data['ejection_fraction'] = request.form['ejection_fraction'].value
    data['serum_creatinine'] = request.form['serum_creatinine'].value
    data['time'] = request.form['time'].value

    if prediction == 1:
      data['status'] = "Meninggal"
      data['result'] = 'Berdasarkan record tersebut, orang yang bersangkutan sudah meninggal'
    else:
      data['status'] = "Hidup"
      data['result'] = 'Berdasarkan record tersebut, orang yang bersangkutan tidak meninggal'

    #return render_template('index.html', prediction_text='{}'.format(result))
    return render_template('index.html', **data)


if __name__ == "__main__":
    app.run(debug=True)