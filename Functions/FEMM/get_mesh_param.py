# -*- coding: utf-8 -*-
"""@package get_element_size_from_label
@date Created on août 09 14:00 2018
@author franco_i
"""


def get_mesh_param(label, FEMM_dict):
    """Returns main mesh parameters corresponding to a surface label

    Parameters
    ----------
    label : str
        label of the surface to assign
    FEMM_dict : dict
        Dictionnary containing the main parameters of FEMM

    Returns
    -------
    mesh_dict : dict
        dictionnary containing the main mesh parameters of the surface
    
    """

    mesh_dict = dict()

    # Default automesh except airgap
    mesh_dict["automesh"] = FEMM_dict["automesh"]

    if "Lamination_Stator" in label:  # Stator
        if "bore" in label:
            mesh_dict["element_size"] = FEMM_dict["elementsize_slotS"]
        else:
            mesh_dict["element_size"] = FEMM_dict["elementsize_yokeS"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SC"]
    elif "Lamination_Rotor" in label:  # Rotor
        if "bore" in label:
            mesh_dict["element_size"] = FEMM_dict["elementsize_slotR"]
        else:
            mesh_dict["element_size"] = FEMM_dict["elementsize_yokeR"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RC"]
    elif "Ventilation" in label:  # Ventilation
        mesh_dict["element_size"] = FEMM_dict["maxelementsize"]
        if label[12] == "S":  # if the Ventilation is on the Stator
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SV"]
        else:  # if the Ventilation is on the Rotor
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RV"]
    elif "Wind" in label:  # Winding on the Lamination
        if label[4] == "S":  # if the winding is on the Stator
            mesh_dict["element_size"] = FEMM_dict["elementsize_slotS"]
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SW"]
        else:  # if the winding is on the Rotor
            mesh_dict["element_size"] = FEMM_dict["elementsize_slotR"]
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RW"]
    elif "Magnet" in label:  # Magnet
        if label[6] == "S":  # if the Magnet is on the Stator
            mesh_dict["element_size"] = FEMM_dict["elementsize_magnetS"]
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_SW"]
        else:  # if the Magnet is on the Rotor
            mesh_dict["element_size"] = FEMM_dict["elementsize_magnetR"]
            mesh_dict["group"] = FEMM_dict["groups"]["GROUP_RW"]
    elif "Airgap" in label:
        mesh_dict["automesh"] = FEMM_dict["automesh_airgap"]
        mesh_dict["element_size"] = FEMM_dict["elementsize_airgap"]
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_AG"]
    elif "No_mesh" in label:
        mesh_dict["automesh"] = FEMM_dict["automesh_airgap"]
        mesh_dict["element_size"] = 0
        mesh_dict["group"] = FEMM_dict["groups"]["GROUP_AG"]
    return mesh_dict
