# ParAMS runscript examples
This repository contains a few simple, documented run-scripts to use plams and ParAMS. These are, more or less, specifically aimed to be used on computers on the IFP-network (i.e. that can access the IFP-licenses and cluster). Moreover, minimal bash-scripts to run the calculations on the IFP-cluster are provided as well.

## Installation
There is no need of installation of python, plams or ParAMS, as they are packed with the AMS package. The majority of the most important packages are already installed (such as *numpy*) and are accessible by running amspython. Other packages for more advanced scripts can also be installed, but exceeds the purpose of this introduction.

## Plams
Python Library for Automating Molecular Simulations is the python interface to AMS. Plams allows to automate a lot of tasks.

## ParAMS
Parameterization Tools for AMS is the main program to optimize parameters. Apart from this, it contains many useful converting modules.

## Useful Commands and Tools
All commands below assume that the AMS module is loaded or the path is set locally.

* ```$ kfbrowser``` : allows to open *.rkf* files with a GUI to view the numerical properties
* ```$ amsmovie``` : allows to view the different steps as a small video with the corresponding step interval. Also includes plotting functions of multiple properties.

## Useful links:
* [Python stack in AMS](https://www.scm.com/doc/Scripting/GettingStarted.html)
* [ParAMS documentation](https://www.scm.com/doc/params/index.html)
* [Plams documentation](https://www.scm.com/doc/plams/index.html?highlight=plams)