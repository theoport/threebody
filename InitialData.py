import numpy as np

body1_mass = 1.1  # Alpha Centauri A
body2_mass = 0.907  # Alpha Centauri B

body1_position = np.array([-0.5, 0, 0], dtype="float64")
body2_position = np.array([0.5, 0, 0], dtype="float64")

body1_velocity = np.array([0.01, 0.01, 0], dtype="float64")
body2_velocity = np.array([-0.05, 0, -0.1], dtype="float64")

body1_momentum = body1_velocity * body1_mass
body2_momentum = body2_velocity * body2_mass

total_momentum = body1_momentum + body2_momentum

body1_adjusted_velocity = (body1_momentum - total_momentum/ 2) / body1_mass
body2_adjusted_velocity = (body2_momentum - total_momentum/ 2) / body2_mass