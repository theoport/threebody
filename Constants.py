# Define universal gravitation constant
G = 6.67408e-11  # N-m2/kg2

# Reference quantities
m_nd = 1.989e+30  # kilogram | mass of the sun
r_nd = 5.326e+12  # meter | distance between stars in Alpha Centauri
v_nd = 30000  # meter/second | relative velocity of earth around the sun
t_nd = 79.91 * 365 * 24 * 3600 * 0.51  # seconds | orbital period of Alpha Centauri

# Net constants
K1 = G * t_nd * m_nd / (r_nd ** 2 * v_nd)
K2 = v_nd * t_nd
