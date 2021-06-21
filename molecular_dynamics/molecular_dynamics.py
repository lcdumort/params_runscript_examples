#!/usr/bin/env amspython

"""
author: Loic Dumortier
email: loic.dumortier@ifpen.fr OR loic.dumortier@ugent.be
date: 16/06/2021
description: A minimal example to do Molecular Dynamics with an NHC thermostat and ReaxFF as engine.
"""

# Necessary packages for everything to run well
from scm.plams import *
from scm.params import *
import numpy as np
import os

init()  # keep

# input files
ffield = '/path/to/ffield'
geofile = 'path/to/geo'

# nprocs = 6 # autoconfigures
# configs
# Togle parallel on (True) or off (False)
jr = JobRunner(parallel=True, 
               maxjobs=0)

# setting up the molecular dynamics
s.input.ams.Task = 'MolecularDynamics'
s.input.ams.MolecularDynamics.Nsteps = 500
s.input.ams.MolecularDynamics.TimeStep = 0.1
s.input.ams.MolecularDynamics.InitialVelocities.Temperature = 10

# Setting up the thermostat
s.input.ams.MolecularDynamics.Thermostat.Type = 'NHC'
s.input.ams.MolecularDynamics.Thermostat.Temperature = 10
s.input.ams.MolecularDynamics.Thermostat.Tau = 15

# Setting up the engine and forcefield
s.input.reaxff.ForceField = ffield
s.input.reaxff.TaperBO = True


# Collecting the geo-file
JC = geo_to_params(geofile,
                   normal_run_settings=s)
jobs = JC.to_amsjobs()
# All the generated jobs will be available under jobcollection.yaml
JC.store('jobcollection.yaml')
results = [j.run(jobrunner=jr) for j in jobs]

# keep
finish()
