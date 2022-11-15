import numpy as np

#here a function to set initial velocities yielding desired orbits
def set_initial_velocities(r1, r2, m1, m2, e) :
    r = r2 - r1


    #calculate normal vector to plane of rotiation (ez if stars have same z-coord)
    if r[2] == 0 :
        n = np.array([0,0,1])
    else :
        n = np.array([1, 1, -(r[0] + r[1])/r[2]])
        n = n/np.linalg.norm(n)

    #calculate directions of inital velocity (choose antiparallel)
    v2 = np.cross(n,r)
    v2 = v2/np.linalg.norm(v2)
    v1 = -v2

    #calculate initial speeds
    M = m1 + m2
    mu = m1*m2 /M
    v2 *= mu/m2 * np.sqrt((1 + e) *M/np.linalg.norm(r))
    v1 *= mu/m1 * np.sqrt((1 + e) *M/np.linalg.norm(r))

    return v1, v2

body1_mass = 1.1    # Alpha Centauri A
body2_mass = 0.907  # Alpha Centauri B
eccentricity = 0.3    # determines orbital shape: e=0 makes circle, 0<e<1 makes ellipse, e>= 1 is unbound trajectory
velocities_manual = 0


body1_position = np.array([-1/2, 0, 0.2], dtype="float64")
body2_position = np.array([1/2, 0, -0.2], dtype="float64")

if velocities_manual :
    body1_velocity = np.array([0, -1, 0], dtype="float64")
    body2_velocity = np.array([0, 1, 0], dtype="float64")

    #correct velocities to yield 0 total momentum
    body1_momentum = body1_velocity * body1_mass
    body2_momentum = body2_velocity * body2_mass

    total_momentum = body1_momentum + body2_momentum

    body1_velocity = (body1_momentum - total_momentum/ 2) / body1_mass
    body2_velocity = (body2_momentum - total_momentum/ 2) / body2_mass

else :
    body1_velocity, body2_velocity = set_initial_velocities(body1_position, body2_position, body1_mass, body2_mass, eccentricity)