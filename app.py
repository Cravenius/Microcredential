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
    result = ""
    
    if prediction == 1:
      result = 'Akan meninggal karena gagal jantung'
    else:
      result = 'Tidak akan Meninggal karena gagal jantung'

    return render_template('index.html', prediction_text='{}'.format(result))


if __name__ == "__main__":
    app.run(debug=True)