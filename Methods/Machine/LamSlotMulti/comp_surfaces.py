# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlotMulti.comp_surfaces
Lamination with empty Slot computation of all surfaces method
@date Created on Mon Jan 12 17:09:42 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi
from pyleecan.Classes.Lamination import Lamination


def comp_surfaces(self):
    """Compute the Lamination surfaces (Lamination, Ventilation, Slot).

    Parameters
    ----------
    self : LamSlotMulti
        A LamSlotMulti object

    Returns
    -------
    S_dict: dict
        Lamination surface dictionnary (Slam, Svent, Sslot) [m**2]

    """

    S_dict = Lamination.comp_surfaces(self)
    Sslot = 0
    for slot in self.slot_list:
        Sslot += slot.comp_surface()

    S_dict["Sslot"] = Sslot
    S_dict["Slam"] -= Sslot
    return S_dict
