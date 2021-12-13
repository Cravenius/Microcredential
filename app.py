import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('modelRF.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])

def output_string(output):
    if output == 1:
        return 'Berdasarkan record tersebut, orang yang bersangkutan sudah meninggal'
    else:
    	return 'Berdasarkan record tersebut, orang yang bersangkutan tidak meninggal'

def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    result = output_string(prediction)

    return render_template('index.html', prediction_text='The predicted iris flower is {}'.format(result))


if __name__ == "__main__":
    app.run(debug=True)