![HPEDEVLogo](Pictures/wod-logo.png)

# Welcome to Hack Shack
Powered by [HPE Developer Community Team](https://hpedev.io)

# HPE Developer Workshops-on-Demand

# An introduction to HPE Cray Programming Environment (CPE)

*Version: HPE HPC CCPE Tutorial, 1.4*

In this workshop, you will learn basic of using CPE to develop and analyze high-performance codes and workflows.  

# Authors: [Jonathan Sparks](mailto:jonathan.sparks@hpe.com), [Denis Choukroun](mailto:denis.choukroun@hpe.com)

<p align="center">
  <img src="Pictures/hackshackdisco.png">
  
</p>

## Handouts
Workshop-on-Demand Workshops are delivered through a central point that allows a portable, dynamic version of the lab guides. Rather than using standard PDF files which always end in copy / paste errors from the lab guide into the TS sessions, this year we decided to innovate and introduce a brand-new infrastructure. We will leverage a JupyterHub server on which all the different lab guides will be stored in a notebook format (*.ipynb).

You can freely copy the Jupyter Notebooks, including their output, in order to practice back at your office at your own pace, leveraging a local installation of Jupyter Notebook on your laptop.
- You install the Jupyter Notebook application from [here](https://jupyter.org/install). 
- A Beginners Guide is also available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)


Enjoy the labs ! :-)


# Cray Programming Environment Container lab

This workshop lab covers using Cray PE in a container for code development and analysis as well as using both [podman](https://podman.io/) and [singularity](https://sylabs.io/) for parallel execution.

Topics covered are, how to compiling code, analyze performance, identify bottlenecks as well as building containers using CPE as a base build files (aka Dockerfile), basics of building container images, and techniques for managing the size of container images, as well as build High Performance containers.

The lab assumes you are familiar with basic Linux shell commands.

Before beginning, please make sure the lab environment is correctly setup by running the two cells below. To run a cell, highlight the cell and press control-enter or click on the "Run" button in the toolbar.


><img src="Pictures/einstein.png" width="50" height="50" />**Note:** _In this workshop, you will use a set of open source tools, such as podman, skepeo and singularity to build, debug, interrogate and execute containers. 
**Note:** we will introduce several different programming tool-chains from standard GNU, to HPE Cray Programming Environment._ 


### **Let's get hands on!**

## Lab 1: CPE environment basics
In this first lab, you will learn the basics of setting up the development environment and who to use modules for interactive use and automate the environment with a container.

* [Lab 1](1-WKSHP-Environment-Basics.ipynb)

## Lab 2: CPE compiler basics
In this first lab, you will learn the basics of using the CPE tool-chain to compile applications.

* [Lab 2](2-WKSHP-Application-Builds.ipynb)

## Lab 3: CPE application analysis
In this first lab, you will learn to use the CPE application analysis tools to profile and identify performance bottle necks in the code.

* [Lab 3](3-WKSHP-Application-Analysis.ipynb)


## Lab 4: Parallel Applications
In this first lab, you will learn to how to build HPC applications using CPE

* [Lab 4](4-WKSHP-Parallel-Applications.ipynb)

## Lab 5: CPE and containers 
In this first lab, you will learn to use CPE in containers

* [Lab 5](5-WKSHP-CPE-Container.ipynb)

## Lab 6: HPC simulation
In this first lab, you will learn how CPE is used to compile a complex simulation

* [Lab 6](6-WKSHP-Complete-Simulation-Leslie3d.ipynb)


## Lab 7: CPE and Spack
In this first lab, you will learn how to use CPE and Spack together

* [Lab 7](7-WKSHP-CPE-Spack.ipynb)


## Join the HPE Developer Community
![QRCode](Pictures/QRCode-HPEDEV.png)

# Thank you!
![grommet.JPG](Pictures/grommet.jpg)
