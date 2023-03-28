import numpy as np
import InitialData as init
import Constants as constants
from typing import List


def differential_equation(eta: List[float], masses: List[float]) -> List[float]:
    number_of_bodies = int(len(eta) / 6)
    acceleration = np.zeros((number_of_bodies, number_of_bodies, 3))
    for i in range(number_of_bodies):
        for j in range(number_of_bodies):
            if j == i:
                continue
            position_1 = eta[3 * i: 3 * i + 3]
            position_2 = eta[3 * j: 3 * j + 3]
            # a1 = K1 * m2 * vector_r / r^3
            acceleration[i, j] = constants.K1 * masses[j] * (position_2 - position_1) / np.linalg.norm(position_2 - position_1) ** 3


    # a[0] = acceleration[0, 0] + ... + acceleration[0,n]
    a = np.sum(acceleration, axis=1)
    a = a.flatten()


    v = constants.K2 * eta[number_of_bodies * 3:]

    return np.concatenate((v, a))
