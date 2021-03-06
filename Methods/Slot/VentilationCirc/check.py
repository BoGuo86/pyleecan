# -*- coding: utf-8 -*-
"""@package Methods.Machine.VentilationCirc.check

@date Created on Wed Dec 09 17:23:03 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def check(self):
    """Make sure that the ventilation parameters are correctly set

    Parameters
    ----------
    self : VentilationCirc
        A VentilationCirc object

    Returns
    -------
    None

    Raises
    _______
    VentilationCircInstanceError
        Zh must be an integer
        H0 must be a float ot int
        D0 must be a float or int
        Alpha0 must be a float ot int
    """

    if not isinstance(self.Zh, int):
        raise VentilationCircInstanceError("Zh must be an integer")
    if not isinstance(self.H0, float) and not isinstance(self.H0, int):
        raise VentilationCircInstanceError("H0 must be a float ot int ")
    if not isinstance(self.D0, float) and not isinstance(self.D0, int):
        raise VentilationCircInstanceError("D0 must be a float or int ")
    if not isinstance(self.Alpha0, float) and not isinstance(self.Alpha0, int):
        raise VentilationCircInstanceError("Alpha0 must be a float ot int")


class VentilationCircInstanceError(Exception):
    """ """

    pass
