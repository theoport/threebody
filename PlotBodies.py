import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import InitialData as init
import OdeSolver as ode
import TwoBody as tb

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection="3d")
eta = init.eta

# plot settings
cms_plot = True


def animate_func(i):
    global eta
    ax.clear()
    x = eta[3 * np.arange(init.number_of_bodies)]
    y = eta[3 * np.arange(init.number_of_bodies) + 1]
    z = eta[3 * np.arange(init.number_of_bodies) + 2]
    colors = np.arange(init.number_of_bodies)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # Setting Axes Limits
    ax.set_xlim3d([-3, 3])
    ax.set_ylim3d([-3, 3])
    ax.set_zlim3d([-3, 3])

    ax.scatter(x, y, z, c=colors)

    eta = ode.runge_kutta(tb.differential_equation, eta, 0.5)



animate = animation.FuncAnimation(fig=fig, func=animate_func, interval=20)
animate.event_source.stop()
animate.event_source.start()

plt.show()
