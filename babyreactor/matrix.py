"""
Matrix docstring
"""
from __future__ import division
import numpy as np


def cartesian(fuel, reflector, group):
    """
    Cartesian operator matrix
    """
    def matrix(material):
        """
        General cartesian material matrix
        """
        dx = material.delta()
        diffusion = material.diffusion[group]
        removal = material.removal(group)
        sections = material.nodes - 1

        diag_val = (removal + 2. * diffusion / dx ** 2)
        offdiag_val = (- diffusion / dx ** 2)

        diag = np.ones(sections) * diag_val
        offdiag = np.ones(sections - 1) * offdiag_val

        matr = np.diag(diag, 0) + np.diag(offdiag, -1) + np.diag(offdiag, 1)
        matr[0, 0] = 0.5 * diag_val

        return matr

    # First make the fuel and reflector matrices
    fuel_matrix = matrix(fuel)
    print(fuel_matrix)
    r = reflector
    reflector_matrix = matrix(reflector)

    # Now join them
    top_left = fuel_matrix
    bottom_right = reflector_matrix[1:][1:]
    top_right = np.zeros((top_left.shape[0], bottom_right.shape[1]))
    bottom_left = np.zeros_like(top_right).transpose()

    top = np.concatenate((top_left, top_right), axis=1)
    bottom = np.concatenate((bottom_left, bottom_right), axis=1)
    everything = np.concatenate((top, bottom), axis=0)

    everything[fuel.nodes - 1][fuel.nodes - 1] =\
            -(1 + (r.diffusion[group] * fuel.delta()) / (fuel.diffusion[group] * r.delta()))
    everything[fuel.nodes - 1][fuel.nodes - 2] = (r.diffusion[group] * fuel.delta()) /\
                                                 (fuel.diffusion[group] * r.delta())
    everything[fuel.nodes - 1][fuel.nodes] = (r.diffusion[group] * fuel.delta()) /\
                                             (fuel.diffusion[group] * r.delta())

    return everything

def cylindrical():
    """
    Cylindrical operator matrix
    """
    pass

def spherical():
    """
    Spherical operator matrix
    """
    pass

def mat(geometry):
    """
    Gives the appropriate function for the matrix
    """

    # Take case out of the equation
    geometry = geometry.lower()

    if geometry == 'cartesian':
        return cartesian
    elif geometry == 'spherical':
        return spherical
    elif geometry == 'cylindrical':
        return cylindrical
    else:
        raise ValueError('Geometry must be \'Spherical\', \'Cylindrical\', or '\
                         '\'Cartesian\'. You selected {0}.'.format(geometry))
