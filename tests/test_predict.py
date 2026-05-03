import numpy as np
from sklearn.preprocessing import MinMaxScaler
from src.model import predict

class DummyModel:
    def predict(self, X):
        return X * 0.5

def test_prepare_input():
    arr = predict.prepare_input([210, 220, 210])
    assert arr.shape == (3, 1)
    assert np.array_equal(arr, np.array([[210], [220], [210]]))

def test_predict_values_with_dummy_model():
    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler.fit(np.array([[0], [100]]))

    model = DummyModel()
    raw, scaled, pred_scaled, pred_raw = predict.predict_values([0, 100], model, scaler)

    assert raw.shape == (2, 1)
    assert scaled.min() >= -1.0
    assert scaled.max() <= 1.0
    assert pred_scaled.shape == (2, 1)
    assert pred_raw.shape == (2, 1)