"""
Matrix docstring
"""
from __future__ import division
import numpy as np


def cartesian():
    """
    Cartesian operator matrix
    """
    pass

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
