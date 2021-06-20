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

trainsetfile = '/work/dumortil/Documents/projects/zeolytes/training_set/trainset.in'
reference = trainset_to_params(trainsetfile)
reference.store('trainingset.yaml')
ffieldfile = '/work/dumortil/Documents/projects/zeolytes/forcefields/1-ffield_Rff1/ffield_Rff1'
parameters = ReaxParams(ffieldfile)
geofile = '/work/dumortil/Documents/projects/zeolytes/structures/geo'

print('Total parameters: {}'.format(len(parameters)))
print('Active paramters: {}'.format(len(parameters.active)))

###################################
# STARTING TO ACTIVATE PARAMETERS #
###################################

# Only select relevant parameters (based on atoms)
atoms = set(['Al', 'O', 'H'])
for param in parameters:
    param.is_active = set(param.atoms).issubset(atoms) and param.is_active

# Counting atom-specific parameters
for param in parameters.active:
    if len(set(param.atoms)) == 1:

# Finding Al-O parameters
atoms = set(['Al', 'O'])
for param in parameters.active:
    param.is_active = set(param.atoms).issubset(atoms)

# Some odd parameters with value 0 are expected to stay at that value
# So these are removed from the optimization selection
for param in parameters.active:
    param.is_active = (param.value != 0)

# Remove atom-independent parameters (assuming those are good)
for param in parameters.active:
    param.is_active = len(param.atoms) != 0
printtotal()

# Deactivate 3 and 4-atom parameters within O atom type (assuming those are irrelevant and should thus not be changed)
for param in parameters.active:
    param.is_active = not ((len(param.atoms) > 2) and (set(param.atoms) == set(['O'])))

# Removing parameters that are eReaxFF dependent
for param in parameters.active:
    param.is_active = not re.search('eReaxFF', param.name)

# remove some standard values for 
for param in parameters.active:
    if re.search('valence', param.name):
        param.is_active = False

for param in parameters.active:
    if re.search('Valency', param.name):
        param.is_active = False

for param in parameters.active:
    if re.search('van der Waals', param.name):
        param.is_active=False

for param in parameters.active:
    if re.search('EEM', param.name):
        param.is_active = False

for param in parameters.active:
    if re.search('Number of lone pairs', param.name):
        param.is_active = False

for param in parameters.active:
    if re.search('Sigma bond covalent radius', param.name):
        param.is_active = True 

for param in parameters.active:
    if re.search('Pi bond covalent radius', param.name):
        param.is_active = False

for param in parameters.active:
    if re.search('Double pi bond covalent radius', param.name):
        param.is_active = False


# unselecting O-O parameters for optimization. Justification: no O2 in the system?
for param in parameters.active:
    param.is_active = (param.atoms != ['O', 'O'])

printtotal()

########################################
#  CONFIGURING THE OPTIMIZATION ITSELF #
########################################

# Defining the optimizer, task and engine for the optimization
callbacks = [Timeout(50*60*60), Logger()] 
optimizer = CMAOptimizer(popsize=10, sigma=0.03)


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
