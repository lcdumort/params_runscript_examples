# ParAMS runscript examples
This repository contains a few simple, documented run-scripts to use plams and ParAMS. These are aimed to be used on computers on the IFP-network (i.e. that can access the IFP-licenses and cluster). All the command and examples are run under linux, although they should be fairly similar on Windows.

## Software
### Installation
There is no particular need of installation of python, plams or ParAMS, as they are packed with the AMS package. The majority of the most important packages are already installed (such as *numpy*) and are accessible by running amspython. Other packages for more advanced scripts can also be installed, but exceeds the purpose of this introduction.

### Plams
<img src="plams.png" alt="plams" width="200"/>

Python Library for Automating Molecular Simulations is the python interface to AMS. Plams allows to automate a lot of tasks.


### ParAMS
<img src="params.svg" alt="params" width="200"/>

Parameterization Tools for AMS is the main program to optimize parameters. Apart from this, it contains many useful converting modules.

> :information_source: Since 18 June, GloMPO has been published under the GPL-license! This is not yet included, but I plan on adding scripts soon.


### Other python packages
Although the amspython already comes with the majority of the scientific python packages, it is always possible that one needs more. this can be done by running 
```bash
amspython -m pip install *package*
```
Doing so will initialize a virtual environment where amspython will also look for source code.
> :information_source: This is not a trivial process on the ener440. For normal functionality, the standard included packages are sufficient. However, if you wish to use GloMPO (which has quite some dependencies that are  not yet included), you need to add packages. Due to security issues, this is not a trivial process and needs some workarounds. Please contact me if you would need this, I can help you set this up. I will also try to add a small tutorial on how to do this as well.


### Output
Multiple files are outputted, although the most important one is by far the *rkf*-file. The different files are summarized below.

#### rkf-files
The output from the calculations is stored in one single binary *.rkf* file. The *rkf* file replaces the old output files, such as the *fort* files. These can be read in using the GUI-tools coming with AMS. It can also be useful to use
```bash
kfbrowser
```
to view the content of the *rkf*-files as a text-based format.

#### dill-files
Another possibility to access the calculation results is by using the dill-files. These are useful when you want to access the results using a python-interpreter. All the information is stored in an AMSobject, but once the python-session or scripts ends, these variables are deleted from memory. The automatically generated dill-file allows to restore the session of the object in a new python shell. This can be useful if you want to analyze the results from the server on your local machine using python.

> :warning: **Dill-files are not suitable for long-term storage** Dill-files are the result of 'pickling', which is transorming a Python-object to a binary format. The file strongly depends on your installed python-interpreter, packages and their versions. When you update your interpreter or packages, it is possible that you can no longer read in the dill-files!


#### out, log and error files
These are human-readible text-files that can serve as a quick view on the results. 
* The output-file will be generated once the calculations are done. They contain rather detailed calculation results. 
* The log-file contains information on the iteration at each step, but is in general quite limited. This file is particarly suited for following the process/convergence of your calculations.
* The error-file is hopefulle rather empty. As expected, whenever an error occurs, it will be saved in this file.


## Useful links:
* [Python stack in AMS](https://www.scm.com/doc/Scripting/GettingStarted.html)
* [ParAMS documentation](https://www.scm.com/doc/params/index.html)
* [Plams documentation](https://www.scm.com/doc/plams/index.html?highlight=plams)

## Notes
I will update this repository with new scripts if requested.