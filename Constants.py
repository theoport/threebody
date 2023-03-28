# Constants in SI units (meters, seconds, kilograms)
G_SI = 6.67408e-11  # N-m2/kg2 or m3/(s2 kg2) | grav.constant
T_SI = 79.91 * 365 * 24 * 3600 * 0.51  # seconds | orbital period of Alpha Centauri
Msun_SI = 1.989e+30  # kilogram | mass of the sun
R_SI = 5.326e+12  # meter | distance between stars in Alpha Centauri

Ve_SI = 30000  # meter/second | relative velocity of earth around the sun

# Conversion factors (program to SI)
P2SI_length = R_SI
P2SI_time = 7,564e-7    # = sqrt(R_SI^3/(G_SI * Msun_SI^2))
P2SI_mass = Msun_SI

K1 = G_SI * T_SI * Msun_SI / (R_SI ** 2 * Ve_SI)
K2 = Ve_SI * T_SI / R_SI
