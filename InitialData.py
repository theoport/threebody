import numpy as np
from typing import List, Tuple


def _create_normalised_initial_conditions(initial_masses: List[float], number_of_bodies: int) -> List[float]:
    velocities = np.zeros((number_of_bodies, 3))
    momenta = np.zeros((number_of_bodies, 3))
    total_momentum = np.zeros(3)

    for i in range(number_of_bodies):
        velocities[i] = 0.1 * np.random.rand(3)
        momenta[i] = velocities[i] * initial_masses[i]
        total_momentum += momenta[i]

    for i in range(number_of_bodies):
        momenta[i] = momenta[i] - total_momentum / number_of_bodies
        velocities[i] = momenta[i] / initial_masses[i]

    eta = np.zeros((number_of_bodies * 6))

    # eta looks like [p_x1, p_y1, p_z1, p_x2, p_y2, p_z2, ... v_x1, v_y1, v_z1, v_x2, v_y2, v_z2, ...]
    # where p is position and v is velocity
    for i in range(number_of_bodies):
        # The multiplier 8 seems to generate fairly stable starting positions
        random_position = 8 * np.random.rand(3)
        eta[3 * i] = random_position[0]
        eta[3 * i + 1] = random_position[1]
        eta[3 * i + 2] = random_position[2]
        eta[3 * i + number_of_bodies * 3] = velocities[i][0]
        eta[3 * i + number_of_bodies * 3 + 1] = velocities[i][1]
        eta[3 * i + number_of_bodies * 3 + 2] = velocities[i][2]

    return eta


def _create_initial_masses(number_of_bodies: int) -> float:
    # mass between 0.9 and 1.1
    return 0.9 + np.random.rand(number_of_bodies) / 5

def initial_conditions(number_of_bodies: int) -> Tuple[List[float]]:
    masses = _create_initial_masses(number_of_bodies)
    return (masses, _create_normalised_initial_conditions(masses, number_of_bodies))
