![HPEDEVlogo](Pictures/hpe-dev-logo.png)    ![podmanlogo](Pictures/podman-logo.png)  

# Welcome to the HPE DEV Hack Shack
[WoD Developer Community Team](https://wod.io)

<p align="center">
<img src="Pictures/hackshackdisco.png">

</p>

# WoD Developer Workshop



# Introduction to Podman 101
In this workshop, we’ll go through the fundamentals of containers and Podman, from basic concepts up to running a full containerized web-based application. 

# Authors: [Markus Schreier](mailto:mschreie@redhat.com) & [Frederic Passeron](mailto:frederic.passeron@hpe.com) & [Pablo Preciado](mailto:ppreciad@redhat.com) 

## Handouts
You can freely copy the Jupyter Notebooks, including their output, in order to practice back at your office at your own pace, leveraging a local installation of Jupyter Notebook on your laptop.
- You install the Jupyter Notebook application from [here](https://jupyter.org/install). 
- A Beginners Guide is also available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)

## Objectives of the Podman Lab
At the end of the lab, students should be able to use Podman for running a container, pulling and creating container images, as well as launching an application in it. Also you will be able to understand core security concepts that will help your enterprise to stay safe.

This lab is intended to support a trial and error method so that, during the session, students should fully understand what is behind the tool. Blindly following instructions is not an effective way to learn, IMHO. You've been warned ;-)

Expected duration : 120 minutes

## Reference documents
This workshop is intended to be an introduction into Podman, for a detailed explanation on the funtinality please use Podman documentation: https://docs.podman.io

At the start of each section, there is an estimate of how long it will take to complete.


## Lab flow
The WoD Developer Workshops-on-Demand are delivered through a central point that allows a portable, dynamic version of the lab guides. Rather than using standard PDF files, which always end in copy / paste errors from the lab guide into the TS sessions, this year we decided to innovate and introduce a brand-new infrastructure. We will leverage a JupyterHub server on which all the different lab guides will be stored in a notebook format (*.ipynb).

In a nutshell, a notebook works as follows:

• A notebook is a series of cells

• The notebook uses a kernel (visible in the upper right corner of the notebook)

• A cell can be markdown or code (in the selected kernel)

• To run a cell, use:

    o The Play Button at the top
    o Ctrl-Enter (run and stay on same cell)
    o Shift-Enter (run and move to next cell)
    
• Running a markdown cell is just rendering it

• Running a code cell runs the code and displays the output just below the cell

• When a cell is running, it displays a [*] to its left. Then, when finished, it displays a counter of the number of executions of that cell

• You cannot run a cell when another is already running, but you can interrupt a running cell with the stop button

Enjoy the labs ! :-)

## Workflow

### Lab 1: Introduction to Podman
Description: In this section, we’ll go through some of the basic concepts around Podman and the podman ecosystem.
* [Lab 1](1-WKSHP-Intro-to-Containers-techno.ipynb)

### Lab 2: Starting and stoping a container
Description: In this section, you will execute containerized applications and interact with containers.
* [Lab 2](2-WKSHP-Podman-hello-world.ipynb)

### Lab 3: Managing Container Images
Description: In this section, you will manage, pull and inspect container images.
* [Lab 3](3-WKSHP-Managing-container-images.ipynb)

### Lab 4: Podman security
Description: In this section, we’ll explain some of the core concepts of container security and how use Podman to minimize exposure to attackers.
* [Lab 4](4-WKSHP-Podman-security.ipynb)

### Lab 5: Managing multiple containers
Description: In this section, you will manage multiple continers at the same time  some of the core concepts of container security and how use Podman to minimize exposure to attackers.
* [Lab 5](5-WKSHP-Managing-multiple-containers.ipynb)

### Conclusion
* [Conclusion](6-WKSHP-Conclusion.ipynb)

# Thank you!
![grommet.JPG](Pictures/grommet.JPG)
