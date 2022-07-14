import matplotlib.pyplot as plt
import numpy as np


def rotate(x=np.linspace(-1, 1, 100), y=0.5 * np.linspace(-1, 1, 100), degree=90.0):
    theta = np.pi * degree / 180
    _x = x * np.cos(theta) - y * np.sin(theta)
    _y = x * np.sin(theta) + y * np.cos(theta)
    return _x, _y
