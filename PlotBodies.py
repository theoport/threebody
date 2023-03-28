import matplotlib.pyplot as plt
from matplotlib import animation
from functools import partial
import numpy as np
import InitialData as init
import OdeSolver as ode
import TwoBody as tb
import NBody as nb
from typing import List


def create_plot(number_of_bodies: int):

    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111, projection="3d")
    masses, eta = init.initial_conditions(number_of_bodies)

    # plot settings
    cms_plot = True

    animate = animation.FuncAnimation(fig=fig, func=partial(_animate_func, eta=eta, masses=masses, ax=ax), interval=20)
    animate.event_source.stop()
    animate.event_source.start()

    plt.show()


def _animate_func(i: int, eta: List[float], masses: List[float], ax):
    ax.clear()
    number_of_bodies = int(len(eta) / 6)
    x = eta[3 * np.arange(number_of_bodies)]
    y = eta[3 * np.arange(number_of_bodies) + 1]
    z = eta[3 * np.arange(number_of_bodies) + 2]
    colors = np.arange(number_of_bodies)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim3d([-10, 10])
    ax.set_ylim3d([-10, 10])
    ax.set_zlim3d([-10, 10])

    ax.scatter(x, y, z, c=colors)

    new_eta = ode.runge_kutta(lambda eta: nb.differential_equation(eta, masses), eta, 0.05)
    for i in range(len(new_eta)):
        eta[i] = new_eta[i]


number_of_bodies = int(input('How many bodies do you wanna generate: '))
create_plot(number_of_bodies)