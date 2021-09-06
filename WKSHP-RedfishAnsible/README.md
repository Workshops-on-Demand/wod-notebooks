![HPE DEV Logo](Pictures/hpe-dev-logo.png)

Powered by [HPE DEV Team](https://hpedev.io)

Version 0.120

# Introduction to Redfish Ansible playbooks

[<img src="https://redfish.dmtf.org/sites/default/files/DMTF_Redfish_logo_R.jpg" alt="Redfish Logo" style="width: 125px;"/>](https://redfish.dmtf.org/)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[<img src="Pictures/logo_ansible.png" alt="Ansible logo" style="width: 90px;" />](https://docs.ansible.com/)

## Authors: [François Donzé](francois.donze@hpe.com), [Vincent Berger](vincent.berger@hpe.com)

Feel free to watch Redfish related videos on [YouTube](https://www.youtube.com/playlist?list=PLmYBqUM74OygZjhoZMEZmMP50Od8EfaW8) and read [blogs](https://developer.hpe.com/search?term=redfish) posts.

## Handouts
You can freely copy the Jupyter Notebooks used in this workshop, including their output, in order to practice back at your office at your own pace, leveraging a local installation of Jupyter Notebook on your laptop. To download the notebooks, right click on them in the left sidebar of this Jupyter window and select `Download`.

- You can download the Jupyter Notebook application from [here](https://jupyter.org/install) 
- A Beginners Guide is also available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)

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


## Workshop goals

The goal of this workshop is to present an overview of the management of HPE iLO based servers, including HPE Synergy compute nodes, using Ansible and the Redfish API.

In this workshopw, you will able to perform several exercises against a OneView Data Center Simulator (DCS) and then a SY480 Gen10 Redfish simulator.

## Disclaimer

The material presented in this workshop has been designed to be educative and didactic. Security, error handling, performance, and Python/Ansible best practices have not been correctly implemented on purpose.

## Workshop infrastructure

Each student has a dedicated [Jupyter](https://jupyter.org/) environment hosted by a Linux host that provides a set of [Jupyter Notebooks](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html).

The Jupyter Notebooks have access to an HPE OneView DCS and a [DMTF Redfish server]( https://github.com/DMTF/Redfish-Mockup-Server) providing access to a HPE Synergy iLO 5 mockup.

>Note: Your iLO 5 simulator may not respond exactly like a real ilO 5, but this will not alter the content of the workshop.


## Workshop description

The material available in this workshop consists of the following Jupyter Notebooks. Double click on them sequentially in the left sidebar before reading or executing their content:

- Introduction (this notebook)
- [Lab 1](1-RetrieveOneViewToken.ipynb): Retrieve an HPE OneView Single Sign On iLO 5 session token
- [Lab 2](2-RedfishAnsibleUsingBuiltinUri.ipynb): Redfish Ansible Playbook using on the `uri` built-in module
- [Lab 3](3-RedfishAnsibleUsingHpePlaybooks.ipynb): Redfish Ansible Playbook derived from HPE Playbook examples
- [Lab 4](4-GalaxyModulesAndDmtfPlaybooks.ipynb): Redfish Ansible Playbook with examples using the Ansible Galaxy collection
- [Lab 5](5-RedfishAnsibleUsingIlorest.ipynb): HPE iLOrest Ansible Playbook
- [Conclusion](6-Conclusion.ipynb)
