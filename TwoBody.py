import numpy as np
import Constants as const
import InitialData as init
from typing import List


def differential_equation(eta: List[float]):
    x1 = eta[:3]
    x2 = eta[3:6]
    v1 = eta[6:9]
    v2 = eta[9:12]
    r_vector = x2 - x1
    r = np.linalg.norm(r_vector)

    a1 = const.K1 * (init.masses[1] / r ** 3) * r_vector
    a2 = const.K1 * (init.masses[0] / r ** 3) * r_vector * -1

    return np.concatenate((const.K2 * v1, const.K2 * v2, a1, a2))
