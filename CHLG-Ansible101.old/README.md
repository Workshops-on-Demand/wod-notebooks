![HPElogo](Pictures/element-logo.PNG)


[HPE Developer Community Team](https://hpedev.io)


# Welcome to the HPE Developer Hack Shack


<p align="center">
  <img src="Pictures/hackshackdisco.png">
  
</p>

# HPE Developer Challenge

The challenge consists of:
* A worskhop to complete
* A simple quiz to answer

To complete the workshop, you need to go through the different labs that make up the workshop. Labs are made of cells that needs to be executed. The quiz is related to the workshop you have selected. There are only a few questions to answer (up to 3 maximum).


# ![Ansible](Pictures/Ansiblelogo.png) 
# Ansible 101: A Simple Introduction to Ansible® Concepts                   
When I started my carreer in the IT business more than 20 years ago, an IT admin would usually manage around a few hundred servers. Todays ' figures are incredibly higher.

As a consequence, automation frameworks become  key assets to manage a large number of devices. Ansible is one such automation framework. This workshop is a intended to walk you through the very basics of Ansible; getting it up and running, passing data, fetching information and generally getting comfortable with the basics of how it handles configuration management.

In a nutshell, Ansible is:
* open-source software
* a configuration manager
* simple
* extensible via modules
* written in Python
* used and supported by a broad community
* compatible with many external tools
* a playbook repository
* used by OpenStack, Red Hat Openshift & tons of projects

It supports devices and things you wouldn’t expect:
* Servers, switches and routers (HPE, Aruba, Cisco, Arista, Dell)
* VMware
* Storage devices (HPE, Netapp, Pure Storage, etc.)


If you want to learn more about ansiblen related workshops, take a look at the following:
* [Using the iLO Redfish API with Ansible and HPE OneView](https://hackshack.hpedev.io/workshop/23)


If you want to see more automation related workshops, take a look at the following:
* [Stackstorm 101 - Introduction to the Stackstorm automation features](https://hackshack.hpedev.io/workshop/21)



# Authors:[Frederic Passeron](mailto:frederic.passeron@hpe.com)  and  [Bruno Cornec](mailto:bruno.cornec@hpe.com)

## Handouts
You can freely copy the Jupyter Notebooks, including their output, in order to practice back at your office at your own pace, leveraging a local installation of Jupyter Notebook on your laptop.
- Install the Jupyter Notebook application from [here](https://jupyter.org/install) 
- A Beginners Guide is available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)


## Lab flow
HPE Developer Workshops-on-Demand are delivered through a central point that allows a portable, dynamic version of the lab guides. It leverages a JupyterHub server on which all the different lab guides are stored in a notebook format (*.ipynb).

In a nutshell, a notebook works as follows:

• A notebook is a series of cells

• The notebook uses a kernel (visible in the upper right corner of the notebook)

• A cell can be either markdown or code (in the selected kernel)

• To run a cell use:

    o The Play button at the top
    o Ctrl-Enter (run and stay on same cell)
    o Shift-Enter (run and move to next cell)
    
• Running a markdown cell just renders it

• Running a code cell runs the code and displays the output just below the cell

• When a cell is running, it displays an [*] to its left. Then, when finished, it displays a counter of the number of executions of that cell

• You cannot run a cell when another is already running, but you can interrupt a running cell with the stop button

Enjoy the labs ! :-)


## Workflow

### Lab 1: Architecture
Description: In this section, we’ll go through a quick overview of the different components of Ansible.
* [Lab 1](1-WKSHP-Ansible101-Architecture.ipynb)

### Lab 2: Inventory, Playbooks, and Tasks
Description: In this section, we will see how inventory, playbooks and tasks actually fold together to make Ansible such a great solution.
* [Lab 2](2-WKSHP-Ansible101-Playbooks.ipynb)

### Lab 3: Templates and variables
Description: In this section, we’ll go through some additional Ansible features, like templates and variables.
* [Lab 3](3-WKSHP-Ansible101-Templates.ipynb)

### Lab 4: Roles
Description: In this section, we’ll see some advanced features of Ansible, like roles.
* [Lab 4](3-WKSHP-Ansible101-Roles.ipynb)

### Conclusion: 
* [Conclusion](5-WKSHP-Conclusion.ipynb)

# Thank you!
![grommet.JPG](Pictures/grommet.JPG)


Ansible and the "A" logo is a registered trademark of Red Hat, Inc. in the United States and other countries.


```bash

```
