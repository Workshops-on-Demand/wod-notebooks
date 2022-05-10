![](Pictures/hpedevlogo-NB.jpg)

# Welcome to the HPE Developer Hack Shack
[HPE Developer Community Team](https://hpedev.io)

<p align="center">
  <img src="Pictures/hackshackdisco.png">
  
</p>

# Workshops on Demand

# Advanced PowerShell scripting with HPE OneView Powershell library (POSH) 
![](Pictures/OneView4.png)


# Author: [Dung K Hoang](mailto:dung.hoangkhac@hpe.com)


In this workshop we will explore some advanced features of the OneView PowerShell library as well as techniques to automate OneView deployment using Powershell and the OneView library. Beginners and experts are welcome.

## Prerequisite
The [Hackshack workshop w682](https://hackshack.hpedev.io/replays/8) provides an introduction to the OneView REST API. If you are not familiar with the OneView REST API and the OneView PowerShell library, it is recommended to register for this workshop prior to attend this one.
 
# Lab Flow
HPE Developer Workshops-on-Demand are delivered through a central point that allows a portable, dynamic version of the lab guides. We are now leveraging a jupyterhub server on which all the different labs guides will be stored in a Notebook format (*.ipynb). These Notebooks are accessible from the internet for the event.

Besides, the notebooks can be downloaded to your own laptop for further usage or edition. In order to use  them, you will need to install the jupyter notebook application available [here](https://jupyter.org/install).
Beginners guide available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)

In a nutshell, a notebook works as follows:

• A Notebook is a series de cells

• Notebook uses a kernel (visible in the upper right corner of the Notebook)

• Cell can be Markdown or Code (in the selected kernel)

• To Run a cell use:

    o The Play Button at the top
    o Ctrl-Enter (run and stay on same cell)
    o Shift-Enter (run and move to next cell)
    
• Running a markdown cell is just rendering it

• Running a Code cell runs the code and display the output just below the cell

• When a cell is running it displays a [*] to its left, then when finished, it displays a counter of the number of execution of that cell

• You cannot run a cell when another is already running but you can interrupt a running cell with the stop button

Happy labs ! :-)


# Lab 1: Get information from OneView

In this lab, we will execute several GET-OV commands that query OneView and return various OV resources:
* OV networks with Get-OVnetwork
* OV logical interconnect group with Get-OVLogicalInterconnectGroup

Optionally, you can write a script to collect collect all attributes of a given OV resource in an Excel file. 

* [Lab 1](1-WKSHP-ADVOVPowershell.ipynb)

# Lab 2: Modify / Create OneView resources

Topics of this lab include:
* Modify attributes of OneView resource
* Create new Oneview resource

* [Lab 2](2-WKSHP-ADVOVPowershell.ipynb)







# Thank You!
![grommet.JPG](Pictures/grommet.jpg)

