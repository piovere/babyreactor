"""
Contains configuration and constants used as inputs
"""
import numpy as np
from .material import Material


# int
GROUPS = 2

# FUEL
FUEL = Material()
FUEL.diffusion = np.array([
    1.2627,
    0.3543
])
FUEL.fission = np.array([
    0.003320,
    0.07537
])
FUEL.nu = np.array([
    2.55301,
    2.45642
])
FUEL.absorption = np.array([
    0.01207,
    0.1210
])
FUEL.scattering = np.array([
    [0., 0.01412],
    [0., 0.]
])
FUEL.width = 150.
FUEL.nodes = 4

# REFLECTOR
REFLECTOR = Material()
REFLECTOR.absorption = np.array([
    0.0004,
    0.0197
])
REFLECTOR.fission = np.array([
    0.,
    0.
])
REFLECTOR.nu = np.array([
    0.,
    0.
])
REFLECTOR.diffusion = np.array([
    1.13,
    0.16
])
REFLECTOR.scattering = np.array([
    [0., 0.0494],
    [0., 0.]
])
REFLECTOR.width = 150.
REFLECTOR.nodes = 4
