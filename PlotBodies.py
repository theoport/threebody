import matplotlib.pyplot as plt
import numpy as np
import InitialData as init
import OdeSolver as ode
import TwoBody as tb

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection="3d")
eta = np.concatenate((init.body1_position, init.body1_velocity, init.body2_position, init.body2_velocity))

for i in range(10000):
    print(eta[:3], eta[6:9])
    eta = ode.runge_kutta(tb.differential_equation, eta, 0.01)
    x1 = eta[:3]
    x2 = eta[6:9]
    ax.scatter(x1[0], x1[1], x1[2], color="darkblue")
    ax.scatter(x2[0], x2[1], x2[2], color="tab:red")


plt.show()