import numpy as np
import InitialData as init
import Constants as constants


def differential_equation(y):
    number_of_bodies = int(len(y) / 6)
    acceleration = np.zeros((number_of_bodies, number_of_bodies, 3))
    for i in range(number_of_bodies):
        for j in range(number_of_bodies):
            if j == i:
                continue
            position_1 = y[3 * i: 3 * i + 3]
            position_2 = y[3 * j: 3 * j + 3]
            # distance[2,5] is distance from 2 to 5
            acceleration[i, j] = constants.K1 * init.masses[j] * (position_2 - position_1) / np.linalg.norm(position_2 - position_1) ** 3


    # a[0] = force[0, 0] + ... + force[0,n]
    a = np.sum(acceleration, axis=1)
    a = a.flatten()
    print("a")
    print(a)


    v = constants.K2 * y[number_of_bodies * 3:]
    print("v")
    print(v)

    return np.concatenate((v, a * 3))
