import numpy as np
import InitialData as init
import OdeSolver as ode
import TwoBody as tb
import NBody as nb

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

initial_eta = np.array([ 2.54087693e+00,  3.75123971e+00,  3.77015250e+00,  1.29767135e+00,
         3.27344278e-01,  2.36918467e+00, -1.13599341e-03, -5.91296029e-03,
         8.57645932e-03,  1.23407169e-03,  6.42346765e-03, -9.31692525e-03])

two_body_eta1 =  ode.runge_kutta(tb.differential_equation, initial_eta, 0.05)
n_body_eta1 =  ode.runge_kutta(nb.differential_equation, initial_eta, 0.05)

if ((two_body_eta1 == n_body_eta1).all()):
    print(bcolors.OKGREEN + "Test successful" + bcolors.ENDC)
else:
    print(bcolors.FAIL + "Test failed")
    print("Expected: ")
    print(two_body_eta1)
    print("Actual: ")
    print(n_body_eta1)
    print(bcolors.ENDC)

