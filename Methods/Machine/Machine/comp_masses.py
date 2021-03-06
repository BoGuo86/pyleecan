# -*- coding: utf-8 -*-
"""@package Methods.Machine.Machine.comp_masses
Compute the masses of the machine method
@date Created on Thu Jan 29 13:09:38 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_masses(self):
    """Compute the masses of the machine
    - Mmach : Mass total [kg]
    - Mfra : Mass of the Frame [kg]
    - Msha : Mass of the Shaft [kg]
    - Mrot : Mass dictionnary of the rotor masses
    - Msta : Mass dictionnary of the stator masses

    Parameters
    ----------
    self : Machine
        A Machine object

    Returns
    -------
    M_dict: dict
        A dictionnary of the Machine's masses (Mmach, Msha,
        Mfra, Mrot, Msta) [kg]

    """

    Mfra = self.frame.comp_mass()
    Msha = self.shaft.comp_mass()
    Mrot = self.rotor.comp_masses()
    Msta = self.stator.comp_masses()

    Mtot = Mfra + Msha + Mrot["Mtot"] + Msta["Mtot"]

    return {"Mmach": Mtot, "Mfra": Mfra, "Msha": Msha, "Mrot": Mrot, "Msta": Msta}
