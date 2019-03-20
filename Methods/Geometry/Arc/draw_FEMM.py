# -*- coding: utf-8 -*-
"""@package draw_FEMM
@date Created on juil. 30 15:30 2018
@author franco_i
"""

import femm
from pyleecan.Functions.FEMM import boundary_prop


def draw_FEMM(self, nodeprop=None, maxseg=None, propname=None, hide=False, group=None):
    """Draw the Arc object in FEMM and assign the property

    Parameters
    ----------
    nodeprop :
        Nodal property
         (Default value = None)
    maxseg :
        Meshed with elements that span at most maxsegdeg degrees per element
         (Default value = None)
    propname :
        Boundary property ’propname’
         (Default value = None)
    hide :
        0 = not hidden in post-processor, 1 == hidden in post processor
         (Default value = False)
    group :
        the group the Arc1 object belongs
         (Default value = None)

    Returns
    -------
    None
    """

    # Get BC (if any)
    if self.label in boundary_prop:
        propname = boundary_prop[self.label]

    # Create the nodes
    begin = self.get_begin()
    end = self.get_end()
    X1, Y1 = begin.real, begin.imag
    X2, Y2 = end.real, end.imag
    femm.mi_addnode(X1, Y1)
    femm.mi_selectnode(X1, Y1)
    femm.mi_setnodeprop(nodeprop, group)
    femm.mi_clearselected()
    femm.mi_addnode(X2, Y2)
    femm.mi_selectnode(X2, Y2)
    femm.mi_setnodeprop(nodeprop, group)
    femm.mi_clearselected()

    # Create the arc
    angle = self.get_angle(is_deg=True)
    if angle > 0:
        femm.mi_addarc(X1, Y1, X2, Y2, angle, 2)
    else:
        femm.mi_addarc(X2, Y2, X1, Y1, -angle, 2)
    # Set Arc properties
    Zm = self.get_middle()
    femm.mi_selectarcsegment(Zm.real, Zm.imag)
    femm.mi_setarcsegmentprop(maxseg, propname, hide, group)
    femm.mi_clearselected()