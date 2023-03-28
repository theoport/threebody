import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import InitialData as init
import OdeSolver as ode
import TwoBody as tb
import NBody as nb


def create_plot(config):

    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111, projection="3d")
    eta = config.initial_eta

    # plot settings
    cms_plot = True


    animate = animation.FuncAnimation(fig=fig, func=animate_func, interval=20)
    animate.event_source.stop()
    animate.event_source.start()

    plt.show()


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
    ax.set_xlim3d([-10, 10])
    ax.set_ylim3d([-10, 10])
    ax.set_zlim3d([-10, 10])

    ax.scatter(x, y, z, c=colors)

    eta = ode.runge_kutta(nb.differential_equation, eta, 0.05)
