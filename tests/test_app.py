import numpy as np
from sklearn.preprocessing import MinMaxScaler
from src.model import app

def test_create_seq():
    data = np.array([[1], [2], [3], [4]])
    seq, nxt = app.create_seq(data, window_size=2)

    expected_seq = np.array([[[1], [2]], [[2], [3]]])
    expected_nxt = np.array([[3], [4]])

    assert np.array_equal(seq, expected_seq)
    assert np.array_equal(nxt, expected_nxt)

def test_scale_metric_range():
    metric = np.array([[10], [20], [30]])
    scaled = app.scale_metric(metric)

    assert scaled.min() >= -1.0
    assert scaled.max() <= 1.0
    assert np.allclose(scaled[0], -1.0)
    assert np.allclose(scaled[-1], 1.0)