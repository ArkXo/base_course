import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m = 3
a_0 = 10
gamma = 0.2
t = np.arrange(0, 10**3, 1)

def boost_function():
    a = (np.sqrt(m**2 + 12*gamma*a_0))
