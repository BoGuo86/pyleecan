# -*- coding: utf-8 -*-
"""@package Functions.gen_phase_list
Generate color and name for phase functions
@date Created on Tue Jan 27 14:58:26 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from random import choice

from pyleecan.Methods.Machine import PHASE_COLOR, PHASE_NAME


def gen_color(N):
    """Generate a list of phase color

    Parameters
    ----------
    N : int
        number of color to generate

    Returns
    -------
    Color_list: list
        A list of hexa representation of colors (str)

    """

    color_list = PHASE_COLOR
    if N < len(color_list):
        return color_list[:N]
    else:
        Hexa = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
        ]
        for ii in range(N - len(color_list)):
            color = "#"
            for i in range(6):
                color += choice(Hexa)
            color_list.append(color)
    return color_list


def gen_name(N):
    """Generate a list of phase name

    Parameters
    ----------
    N : int
        number of name the generate

    Returns
    -------
    Name_list: list
        A list of phase name

    """

    Alpha = PHASE_NAME

    Name_list = list()
    for i in range(N):
        name = ""
        if i // 26 > 0:
            name += Alpha[(i // 26) - 1]
        name += Alpha[i % 26]
        Name_list.append(name)

    return Name_list
