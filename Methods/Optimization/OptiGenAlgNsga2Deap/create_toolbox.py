# -*- coding: utf-8 -*-
from pyleecan.Classes.Output import Output
from deap import base, creator, tools


def create_toolbox(self):
    """OptiGenAlgNsga2Deap method to create DEAP toolbox
    Parameters
    ----------
    self : OptiGenAlgNsga2Deap

    Returns
    -------
    self : OptiGenAlgNsga2Deap
        OptiGenAlgNsga2Deap with toolbox created 
    """

    def create_indiv(create, output, design_var):
        """Create individual using DEAP tools
        
        Parameters
        ----------
        creator : function
            function to create the individual
        output : pyleecan.Classes.Output
            output of the individual
        design_var : dict
            Design variables  
            
        Returns:
        --------
        indiv : list
            individual 
        """

        # Extract design variables
        keys = list(design_var.keys())
        var = []

        keys.sort()
        for key in keys:
            tmp = design_var[key].function(design_var[key].space)
            exec(design_var[key].name + "=tmp")
            var.append(tmp)

        ind = create(var)

        # Store the keys
        ind.keys = keys

        # Store the design variables
        ind.design_var = design_var

        # Store the simulation validity
        ind.is_simu_valid = False

        # Store the number of constraints violations
        ind.cstr_viol = 0

        # Output with the design variables set
        ind.output = Output(simu=output.simu.as_dict())

        return ind

    # Create toolbox
    self.toolbox = base.Toolbox()

    # Create Fitness and individual
    creator.create(
        "FitnessMin", base.Fitness, weights=[-1 for _ in self.problem.design_var]
    )
    creator.create("Individual", list, typecode="d", fitness=creator.FitnessMin)

    self.toolbox.register("creator", creator.Individual)

    # Register individual and population
    self.toolbox.register(
        "individual",
        create_indiv,
        self.toolbox.creator,
        self.problem.output,
        self.problem.design_var,
    )

    self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
