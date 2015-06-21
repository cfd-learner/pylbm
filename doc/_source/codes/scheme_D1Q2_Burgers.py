# Authors:
#     Loic Gouarin <loic.gouarin@math.u-psud.fr>
#     Benjamin Graille <benjamin.graille@math.u-psud.fr>
#
# License: BSD 3 clause

"""
Example of a D1Q2 for Burger's
"""
import sympy as sp
import pyLBM
u, X = sp.symbols('u, X')

d = {
    'dim':1,
    'scheme_velocity':1.,
    'schemes':[
        {
            'velocities': range(1,3),
            'conserved_moments':u,
            'polynomials': [1, X],
            'equilibrium': [u, .5*u**2],
            'relaxation_parameters': [0., 1.9],
        },
    ],
}
s = pyLBM.Scheme(d)
print(s)
