import numpy as np


def create_initial_eta(initial_masses, number_of_bodies):
    velocities = np.zeros((number_of_bodies, 3))
    # momenta = np.zeros((number_of_bodies, 3))
    # total_momentum = np.zeros(3)
    # for i in range(number_of_bodies):
    #     # velocities[i] = 2 * np.random.rand(3)
    #     momenta[i] = velocities[i] + initial_masses[i]
    #     total_momentum += momenta[i]
    #
    # for i in range(number_of_bodies):
    #     momenta[i] = momenta[i] - total_momentum / number_of_bodies
    #     velocities[i] = momenta[i] / initial_masses[i]

    eta = np.zeros((number_of_bodies * 6))

    for i in range(number_of_bodies):
        random_position = np.random.rand(3)
        eta[3 * i] = random_position[0]
        eta[3 * i + 1] = random_position[1]
        eta[3 * i + 2] = random_position[2]
        eta[3 * i + number_of_bodies * 3] = velocities[i][0]
        eta[3 * i + number_of_bodies * 3 + 1] = velocities[i][1]
        eta[3 * i + number_of_bodies * 3 + 2] = velocities[i][2]

    return eta


def create_initial_masses(number_of_bodies):
    return np.full(number_of_bodies, 0.5)
    # return np.random.rand(number_of_bodies) / 2 + 0.5


number_of_bodies = 2

masses = create_initial_masses(number_of_bodies)
eta = create_initial_eta(masses, number_of_bodies)
