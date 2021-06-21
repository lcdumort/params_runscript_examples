#!/usr/bin/env amspython

"""
author: Loic Dumortier
email: loic.dumortier@ifpen.fr OR loic.dumortier@ugent.be
date: 16/06/2021
description: A minimal example to perform a geometry optimization with FIRE and ReaxFF as engine.
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
jr = JobRunner(parallel=True, maxjobs=0)

# ams settings
s = Settings()
s.input.ams.Task = 'GeometryOptimization'
s.input.ams.geometryoptimization.Method = 'FIRE'
s.input.ams.geometryoptimization.MaxIterations = 10000
s.input.ams.moleculardynamics.pretend_converged = True
s.input.reaxff.ForceField = ffield

# uncomment below to lock each job to one thread only.
# If left commented: each job will run sequentially
# and use all available cores to optimize.
# s.runscript.nproc = 1

# Collecting the geo-file
JC = geo_to_params(geofile,
                   normal_run_settings=s)
jobs = JC.to_amsjobs()
# All the generated jobs will be available under jobcollection.yaml
JC.store('jobcollection.yaml')
results = [j.run(jobrunner=jr) for j in jobs]

# keep
finish()
