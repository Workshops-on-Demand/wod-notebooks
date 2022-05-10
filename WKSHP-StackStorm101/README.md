![HPEDEVlogo](Pictures/hpe-dev-logo.png)  ![StackStormlogo](Pictures/stackstorm.jpg)


# Welcome to the HPE Developer Hack Shack
[HPE Developer Community Team](https://hpedev.io)

<p align="center">
  <img src="Pictures/hackshackdisco.png">
  


# HPE Developer Workshop



# Introduction to StackStorm101
This notebook will walk you through some of the basics of stackstorm. This notebook has been developed to accomodate mutiple users logging into the same stackstorm server. This is not by any means a super deep dive but hopefully will explain why stackstorm should be in your automation toolbag. 

# Author: [Rick A kauffman](mailto:rick.a.kauffman@hpe.com) adaptation by [Frederic Passeron](mailto:frederic.passeron@hpe.com)

## Handouts
You can freely copy the Jupyter Notebooks, including their output, in order to practice back at your office at your own pace, leveraging a local installation of Jupyter Notebook on your laptop.
- You install the Jupyter Notebook application from [here](https://jupyter.org/install). 
- A Beginners Guide is also available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)


## Lab flow
HPE Developer Workshops-on-Demand are delivered through a central point that allows a portable, dynamic version of the lab guides. Rather than using standard PDF files which always end in copy / paste errors from the lab guide into the TS sessions, this year we decided to innovate and introduce a brand-new infrastructure. We will leverage a JupyterHub server on which all the different lab guides will be stored in a notebook format (*.ipynb).

## WARNING! To learn stackstorm we have to start at the bottom. Bear with me to the end and we can explore stackstorm a different way.

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

Enjoy the labs ! :-)


## Workflow

### Lab 1: The Basics
Description: In this section, we’ll go through some of the main concepts behind StackStorm. StackStorm is an automation framework that uses Sensors to watch and listen to alarm/event queues. Triggers to tell Rules when to launch, Actions/Workflows to change the existing state.
* [Lab 1](1-WKSHP-Stackstorm_Basics.ipynb)

![grommet.JPG](Pictures/grommet.JPG)

<h2>Next&nbsp;&nbsp;&nbsp;&nbsp;<a href="1-WKSHP-Stackstorm_Basics.ipynb#sc" target="New" title="Next: Lab1"><i class="fas fa-chevron-circle-right" style="color:#FFAD33;"></i></a></h2>
