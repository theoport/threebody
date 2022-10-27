import numpy as np
import Constants as const
import InitialData as init


def differential_equation(y):
    x1 = y[:3]
    v1 = y[3:6]
    x2 = y[6:9]
    v2 = y[9:12]
    r_vector = x2 - x1
    r = np.linalg.norm(r_vector)

    a1 = const.K1 * (init.body2_mass / r ** 3) * r_vector
    a2 = const.K1 * (init.body1_mass / r ** 3) * r_vector * -1

    return np.concatenate((const.K2 * v1, a1, const.K2 * v2, a2))
