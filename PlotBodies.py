import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import InitialData as init
import OdeSolver as ode
import TwoBody as tb

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection="3d")
eta = np.concatenate((init.body1_position, init.body1_velocity, init.body2_position, init.body2_velocity))


def animate_func(i):
    global eta
    ax.clear()
    eta = ode.runge_kutta(tb.differential_equation, eta, 0.01)
    x1 = eta[:3]
    x2 = eta[6:9]
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # Setting Axes Limits
    ax.set_xlim3d([-1, 1])
    ax.set_ylim3d([-1, 1])
    ax.set_zlim3d([-1, 1])
    rcom_sol = (init.body1_mass * x1 + init.body2_mass * x2) / (init.body1_mass + init.body2_mass)
    # Find location of Alpha Centauri A w.r.t COM
    r1com_sol = x1 - rcom_sol
    # Find location of Alpha Centauri B w.r.t COM
    r2com_sol = x2 - rcom_sol
    ax.scatter(r1com_sol[0], r1com_sol[1], r1com_sol[2], color="darkblue")
    ax.scatter(r2com_sol[0], r2com_sol[1], r2com_sol[2], color="tab:red")


animate = animation.FuncAnimation(fig=fig, func=animate_func, interval=50)
animate.event_source.stop()
animate.event_source.start()

plt.show()
