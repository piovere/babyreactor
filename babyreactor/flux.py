"""@package docstring
Documentation for this module

More details
"""

from __future__ import division
import numpy as np


def iterate_flux(flux_old, matrix, k_old, fission):
    """
    The next iteration of the flux

    Produces the next iteration of the flux using the method on page 5-279 of
    Deuderstadt and Hamilton's book.

    Parameters
    ----------
    flux : numpy.ndarray
        Array containing the flux value at each node
    matrix : numpy.ndarray
        2-d array with the removal operator
    k : float
        Neutron multiplication constant for the reactor
    fission: numpy.ndarray
        Fission constants for each node

    Returns
    -------
    tuple
        next flux iteration, next k iteration, error in
        the flux (really deviation between generations), generational
        change in k
    """
    source = np.multiply(flux_old, fission) / k_old

    flux_new = np.linalg.solve(matrix, source)

    mag_old = np.linalg.norm(flux_old)
    mag_new = np.linalg.norm(flux_new)

    k_new = k_old * mag_new / mag_old

    flux_error = abs(mag_new - mag_old) / mag_new
    k_error = abs(k_new - k_old) / k_new

    return flux_new, k_new, flux_error, k_error
