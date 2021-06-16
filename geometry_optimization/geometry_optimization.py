#!/usr/bin/env amspython

from scm.plams import *
from scm.params import *
import numpy as np
import os

init()  # keep

# input files
# Change to relevant Force Field
ffield = ('/work/dumortil/Documents/projects/'
          'zeolytes/Al_Si_O/training_set/ff1/ffield')
# Change to relevant Geofile
geofile = './geo'
# nprocs = 6 # autoconfigure

# configs
# Togle parallel on (True) or off (False)
jr = JobRunner(parallel=True, maxjobs=0)

# ams settings
s = Settings()
# Keep for geometry optimization
s.input.ams.Task = 'GeometryOptimization'
# Configure geometry optimization method
s.input.ams.geometryoptimization.Method = 'FIRE'
# Max iterations for optimizer
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
results = [j.run(jobrunner=jr) for j in jobs[:7]]

# keep
finish()
