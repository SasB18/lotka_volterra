"""
Solution for the Lotka-Volterra equations (predator-prey model)
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# declare initial values
preys = 4
predators = 2

X0 = [preys, predators]

t = np.arange(1, 20, .1)

a = 1
b = 1
c = 1
d = 1

def model(N, t):
    """Model for the Lotka-Volterra equations

    parameters:
    x: no. preys
    y: no. predators
    t: time (independent variable)
    a, b, c, d: arbitary constants for the differential equations
    """
    x, y = N
    # equation for the no. preys over time
    dxdt = (a - b*y) * x
    # equation for the no. predators over time
    dydt = (c*x - d) * y
    # returns the set of differential equations
    return [dxdt, dydt]

solution = integrate.odeint(model, X0, t)
x, y = solution.T

fig, ax = plt.subplots(1, 2)

ax[0].plot(t, x); ax[0].plot(t, y)
ax[0].set_title("Population size in time")
ax[0].set_ylabel("no. species")
ax[0].set_xlabel("time")

ax[1].plot(x, y)
ax[1].set_title("Population size in phase space")
ax[1].set_ylabel("no. preys")
ax[1].set_xlabel("no. predators")

ax[0].grid(); ax[1].grid() 
plt.show()


