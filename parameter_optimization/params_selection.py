#~/ams2021.202.r94433/bin/amspython

from scm.params import *
from scm.plams import *
import numpy as np
import re

#######################################
# FUNCTION TO COUNT ACTIVE PARAMETERS #
#######################################

def printtotal():
    global parameters
    print('Total parameters: {}'.format(len(parameters)))
    print('Active paramters: {}'.format(len(parameters.active)))

#######################################
# DEFINING TRAINNGSETS AND FORCEFIELD #
#######################################

trainsetfile = '/path/to/trainset.in'
reference = trainset_to_params(trainsetfile)
reference.store('trainingset.yaml')
ffieldfile = '/path/to/ffield'
geofile = '/path/to/geo'

parameters = ReaxParams(ffieldfile)
print('Total parameters: {}'.format(len(parameters)))
print('Active paramters: {}'.format(len(parameters.active)))

###################################
# STARTING TO ACTIVATE PARAMETERS #
###################################

# Untoggle to deselect all parameters
#for param in parameters:
#    param.is_active = False

to_activate = [
    'list parameters to activate as strings'
]

for param in parameters:
    if param.name in to_activate:
        param.is_active = True 

# Add some more parameter selection criterias

printtotal()

########################################
#  CONFIGURING THE OPTIMIZATION ITSELF #
########################################

# Defining the optimizer, task and engine for the optimization
callbacks = [Timeout(50*60*60), 
             Logger()] 
optimizer = CMAOptimizer(popsize=10, sigma=0.03)



# Redefine the task you want to optimize
s = Settings()
s.input.ams.Task = 'GeometryOptimization'
s.input.ams.geometryoptimization.Method = 'FIRE'
s.input.ams.geometryoptimization.MaxIterations =100 


JC = geo_to_params(geofile, normal_run_settings=s)
JC.store('jobcollection.yaml')

############################
# RUNNING THE OPTIMIZATION #
############################

optim = Optimization(JC, reference, parameters, optimizer, callbacks=callbacks, skip_x0=True)
v = optim.optimize()
