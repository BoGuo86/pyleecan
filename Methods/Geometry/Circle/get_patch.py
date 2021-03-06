# -*- coding: utf-8 -*-
from matplotlib.patches import Circle

from pyleecan.Methods.Machine import (
    PATCH_COLOR,
    PATCH_EDGE,
    PATCH_COLOR_ALPHA,
    PATCH_EDGE_ALPHA,
)


def get_patch(self, color=PATCH_COLOR, edgecolor=PATCH_EDGE, is_edge_only=False):
    """Returns the Circle Patch to be display in matplotlib

    Parameters
    ----------
    self : Circle
          a Circle object
    color :
        the color of the Patch (Default value = PATCH_COLOR)
    edgecolor :
        edgecolor of the Patch (Default value = PATCH_EDGE)
    is_edge_only: bool
        To set the transparancy of the face color to 0 and 1 for the edge color

    Returns
    -------
    patch : matplotlib.patches.Circle
        The patch corresponding to the surface
    """

    # check if the Circle is correct
    self.check()
    # the coordinates of the center of the circle
    Zr = self.center.real
    Zi = self.center.imag

    if is_edge_only:
        color = PATCH_COLOR_ALPHA
        edgecolor = PATCH_EDGE_ALPHA

    return Circle(xy=(Zr, Zi), radius=self.radius, facecolor=color, edgecolor=edgecolor)
