
from tensorflow.keras.models import load_model
from tensorflow.keras.metrics import MeanSquaredError
import numpy as numpy
import joblib

Scaler_Path = "scaler.save"
Model_Path = "model.keras"
def load_scaler_model():
    model = load_model(Model_Path, custom_objects={'mse': MeanSquaredError})
    scaler = joblib.load(Scaler_Path)
    return model,scaler

def predict(model,scaler,value):
    value = numpy.array(value).reshape(-1,1)
    scaled = scaler.transform(value)
    predict_scale = model.predict(scaled)
    predict_value = scaler.inverse_transform(predict_scale)
    print("raw input:", value)
    print("scaled input:", scaled)
    print("prediction scaled:", predict_scale)
    print("prediction raw:", predict_value)
    return predict_value

if __name__ == "__main__":
    print("-----------------------------PREDICT START---------------------------------------")
    model,scaler = load_scaler_model()
    value= [250,260,250]
    predict(model,scaler,value)
    print("-----------------------------PREDICT DONE---------------------------------------")   


