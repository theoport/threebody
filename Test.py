import numpy as np
import InitialData as init
import OdeSolver as ode
import TwoBody as tb

eta = init.eta
eta1 =  ode.runge_kutta(tb.differential_equation, eta, 0.05)
eta2 =  ode.runge_kutta(tb.differential_equation, eta, 0.05)
eta3 =  ode.runge_kutta(tb.differential_equation, eta, 0.05)

print(eta1)
print(eta2)
print(eta3)
