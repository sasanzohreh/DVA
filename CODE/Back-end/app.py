from flask import Flask, request
from flask_cors import CORS
import os
import json
from helpers import *
import pickle

app = Flask(__name__)
CORS(app)



@app.route("/test")
def verify_backend_alive():
    return {"Status": "Backend is alive"}

@app.route("/yellow_taxi_pred", methods = ["POST"])
def get_yellow_taxi_predictions():
    try:
        # make predictions
        params = json.loads(request.data)
        preds = get_predictions(params,taxi_model)

        # save predictions as json file
        with open('../Front-end/index/taxi_predictions.json', 'w') as fp:
            json.dump(preds, fp)

        # return output
        return preds

    except Exception as e:
        #print(e)
        return e
    
@app.route("/bike_pred", methods = ["POST"])
def get_bike_predictions():
    try:
        # make predictions
        params = json.loads(request.data)
        preds = get_predictions(params,bike_model)

        # save predictions as json file
        with open('../Front-end/index/bike_predictions.json', 'w') as fp:
            json.dump(preds, fp)

        # return output
        return preds

    except Exception as e:
        #print(e)
        return e
    
@app.route("/fhv_pred", methods = ["POST"])
def get_fhv_predictions():
    try:
        # make predictions
        params = json.loads(request.data)
        preds = get_predictions(params,fhv_model)

        # save predictions as json file
        with open('../Front-end/index/fhv_predictions.json', 'w') as fp:
            json.dump(preds, fp)

        # return output
        return preds

    except Exception as e:
        #print(e)
        return e


if __name__ == "__main__":
    print("Backend starting")

    # load models
    with open('../Modelling/yellow_taxi_model.pkl', 'rb') as f:
        taxi_model = pickle.load(f)
    with open('../Modelling/bike_data_model.pkl', 'rb') as f:
        bike_model = pickle.load(f)
    with open('../Modelling/fhvhv_model.pkl', 'rb') as f:
        fhv_model = pickle.load(f)

    # run app
    app.run(debug=False)