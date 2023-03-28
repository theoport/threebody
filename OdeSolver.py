from typing import List, Callable

def runge_kutta(differential: Callable[[List[float], List[float]], List[float]],  eta: List[float], delta_t: float):
    y0 = eta
    k0 = differential(y0)
    y1 = y0 + k0 * delta_t / 2
    k1 = differential(y1)
    y2 = y0 + k1 * delta_t / 2
    k2 = differential(y2)
    y3 = y0 + k2 * delta_t
    k3 = differential(y3)
    k = (1 / 6) * (k0 + 2 * k1 + 2 * k2 + k3)
    return y0 + k * delta_t
