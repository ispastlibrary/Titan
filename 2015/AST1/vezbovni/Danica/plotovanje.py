import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

D, V, greskapoy=np.loadtxt('plotovanje.txt' , unpack=True)

def fun(a,b):
    return a/b

