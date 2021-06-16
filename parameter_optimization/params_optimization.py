import numpy as np

from scm.params import *
from scm.plams import *
# DataSet for storing the results
DS_results = DataSet()

# Defining the optimizer and callbacks
optimizer = CMAoptimizer(popsize=10,
                         sigma=0.1,
                         minsigma=5e-4)
callbacks = [Logger(),Timeout(60*25)]

# Defining the task and engine for the optimization
ffield = '/work/dumortil/Documents/projects/zeolytes/forcefields/1-ffield_Rff1/ffield_Rff1'
s = Settings()
s.input.ams.Task = 'GeometryOptimization'
s.input.ams.geometryoptimization.Method = 'FIRE'

e = Engine()
e.settings.input.ReaxFF
e.settings.input.forcefield = ffield
