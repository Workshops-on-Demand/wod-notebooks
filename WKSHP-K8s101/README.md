![HPEDEVlogo](Pictures/hpe-dev-logo.png)

# Welcome to the HPE Developer Hack Shack
[HPE Developer Community Team](https://hpedev.io)

<p align="center">
  <img src="Pictures/hackshackdisco.png">
  
</p>

# HPE Developer Workshop



# Introduction to Kubernetes Basics 
This tutorial provides a walkthrough of the basics of the Kubernetes cluster orchestration system. Each module contains some background information on major Kubernetes features and concepts, and includes interactive labs using a Kubernetes cluster managed by HPE Ezmeral Container Platform.

# Author: [Didier Lalli](mailto:didier.lalli@hpe.com)

## Handouts
You can freely copy the Jupyter Notebooks, including their output, in order to practice back at your office at your own pace, leveraging a local installation of Jupyter Notebook on your laptop.
- You install the Jupyter Notebook application from [here](https://jupyter.org/install). 
- A Beginners Guide is also available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)


## Lab flow
HPE Developer Workshops-on-Demand are delivered through a central point that allows a portable, dynamic version of the lab guides. Rather than using standard PDF files which always end in copy / paste errors from the lab guide into the TS sessions, this year we decided to innovate and introduce a brand-new infrastructure. We will leverage a JupyterHub server on which all the different lab guides will be stored in a notebook format (*.ipynb).

## A quick look at Jupyter Notebook
Jupyter Notebook is an open source solution for interactive documents that are commonly used to hold code for ML/DL models. 
A Notebook consists of cells. A cell can be a markdown cell (contains comments, text, images) or a code cell. 

To execute code within the Notebook, you run each cell in turn by clicking on the ***Play button*** in the menu bar of the Notebook.

> **Note:**  When you see a [*] next to the action it means your execution step is busy working within the notebook. When you see a digit number, it means the execution of the step is completed.  

![QickLookNotebook](Pictures/Quick-look-Notebook.png)

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

• When a cell is running it displays a [*] to its left, then when finished, it displays a counter of the number of executions in the notebook

• You cannot run a cell when another is already running but you can interrupt a running cell with the stop button

Enjoy the labs ! :-)


## Workflow

### [Intro](1-WKSHP-K8S101.ipynb)
### [Module 1: Explore your Kubernetes cluster](2-WKSHP-K8S101-mod1.ipynb)
### [Module 2: Deploy an app](3-WKSHP-K8S101-mod2.ipynb)
### [Module 3: Explore your app](4-WKSHP-K8S101-mod3.ipynb)
### [Module 4: Using a Service to Expose Your App](5-WKSHP-K8S101-mod4.ipynb)
### [Module 5: Scale up your app](6-WKSHP-K8S101-mod5.ipynb)
### [Module 6: Update your app](7-WKSHP-K8S101-mod6.ipynb)
### [Conclusion](8-WKSHP-Conclusion.ipynb)

# Thank you!
![grommet.JPG](Pictures/grommet.JPG)
