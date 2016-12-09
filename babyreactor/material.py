"""
"""


class Material(object):
    """
    """
    def __init__(self):
        self._nodes = None
        self._width = None
        self._fission = None
        self._absorption = None
        self._scattering = None
        self._diffusion = None
        self._nu = None

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, n):
        self._nodes = n

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w

    @property
    def fission(self):
        return self._fission

    @fission.setter
    def fission(self, f):
        self._fission = f

    @property
    def scattering(self):
        return self._scattering

    @scattering.setter
    def scattering(self, s):
        self._scattering = s
    
    @property
    def diffusion(self):
        return self._diffusion

    @diffusion.setter
    def diffusion(self, d):
        self._diffusion = d

    @property
    def nu(self):
        return self._nu

    @nu.setter
    def nu(self, n):
        self._nu = n

    @property
    def absorption(self):
        return self._absorption

    @absorption.setter
    def absorption(self, a):
        return self._absorption
