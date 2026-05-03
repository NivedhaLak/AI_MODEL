from pyexpat import model

import pandas as pandas
import numpy as numpy
from sklearn.preprocessing import MinMaxScaler
import joblib
import tensorflow.keras.models  as models
import tensorflow.keras.layers as layers

CSV_PATH = r"/Users/anshuljain/Desktop/Nivedha/Projects/Python/AI_Model/resource/jena_climate_2009_2016.csv"
MODEL_PATH = "model.keras"
SCALER_PATH = "scaler.save"

def main():
    df = pandas.read_csv(CSV_PATH)    
    metric = df[["Tpot (K)"]].values
    metric = scale_data(metric)
    seq, next = create_seq(metric, 3)
    print(f"Sequence Length: {len(seq)}, Next Length: {len(next)}")
    seq = numpy.array(seq).reshape((len(seq), 3, 1))
    next = numpy.array(next)

    model = create_model()
    model.fit(seq, next, batch_size=50)
    model.save(MODEL_PATH)

def create_model():
    print("-----------------------------MODEL CREATE START---------------------------------------")
    model =models.Sequential()
    model.add(layers.LSTM(1000,input_shape=(3,1)))
    model.add(layers.Dense(1, activation="tanh"))
    model.compile(optimizer="adam",loss="mse")
    print("-----------------------------MODEL CREATE END---------------------------------------")
    return model
def create_seq(data,windowSize):
    print("-----------------------------CREATE SEQUENCE START---------------------------------------")
    seq ,next= [],[]
    for i in range(len(data)-windowSize):
        seq.append(data[i:i+windowSize])
        next.append(data[i+windowSize])
    print("-----------------------------CREATE SEQUENCE DONE---------------------------------------")
    return seq,next

def scale_data(metric):
    scaler = MinMaxScaler(feature_range=(-1,1))
    data = scaler.fit_transform(metric)
    joblib.dump(scaler,SCALER_PATH)
    return data

if __name__ == "__main__":
    main()