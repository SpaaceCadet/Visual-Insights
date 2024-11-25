import requests
import json
from inference.precision import Precise as pr
import numpy as np
from dotenv import load_dotenv
import os
import joblib

# Load env var  For Tf serving
load_dotenv()

tf_host_server = os.getenv("TF_HOST_SERVER")

tf_port_SERVER = os.getenv("TF_PORT_SERVER")


class Model_inference:
    # end_train_date =datetime.strptime('2018-07-18 22:00:00+0000', '%Y-%m-%d %H:%M:%S%z')

    X_test = np.load('./model_params/X_test.npy')

    y_test = np.load('./model_params/y_test.npy')

    scaler_X = joblib.load('./model_params/scaler_x.pkl')
    
    scaler_Y = joblib.load('./model_params/scaler_y.pkl')

    def __init__(self, model):

        self.__model_name = model

    def get_model_name(self):

        return self.__model_name

    def predict(self, nb_forecast, time_scale):
        if (time_scale == "hourly"):
            hours = nb_forecast
        elif (time_scale == "daily"):
            hours = nb_forecast * 24
        elif (time_scale == "monthly"):
            hours = nb_forecast * 24 * 30
        else:
            hours = nb_forecast * 24 * 30 * 365

        # form http rest request

        tf_serving_url = f"http://{tf_host_server}:{tf_port_SERVER}/v1/models/{self.__model_name}:predict"

        # Form the input for the tensorflow serving

        input_data = Model_inference.X_test[:hours, :, :].tolist()  # Replace with your actual input data

        data = {"instances": input_data}

        ## Make the request to TensorFlow Serving

        data = json.dumps(data)

        response = requests.post(tf_serving_url, data=data)

        # Parse the JSON response

        predictions = np.array(json.loads(response.text)["predictions"])

        # Inverse predictions

        inv_forecast = Model_inference.scaler_Y.inverse_transform(predictions)

        inv_y = Model_inference.scaler_Y.inverse_transform(Model_inference.y_test.reshape(-1, 1)).flatten()
        # Compute Performance metrics
        precisions = pr(inv_y[:hours], inv_forecast)

        performance = precisions.performance()

        print(performance)
        return performance, inv_forecast.flatten(), inv_y[:hours]
