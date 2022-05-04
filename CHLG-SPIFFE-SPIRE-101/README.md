![HPElogo](Pictures/element-logo.PNG)


[{{ BRANDING }} Community Team](https://hpedev.io)


# Welcome to the {{ BRANDINGWOD }} Hack Shack


<p align="center">
  <img src="Pictures/hackshackdisco.png">
  
</p>

# {{ BRANDINGWOD }} Challenge

The challenge consists of:
* A worskhop to complete
* A simple quiz to answer

To complete the workshop, you need to go through the different labs that make up the workshop. Labs are made of cells that needs to be executed. The quiz is related to the workshop you have selected. There are only a few questions to answer (up to 3 maximum).

# Introduction to SPIFFE/SPIRE
SPIFFE, the Secure Production Identity Framework for Everyone, is a set of open-source standards for securely identifying software systems in dynamic and heterogeneous environments.

![Spiffe-Spire](Pictures/spire-agent-spiffe-workload1.png)

Enterprise application or software services are increasingly running across multiple platforms spanning multiple data centers and public clouds. Since these services span various domains, the most efficient way to secure them is through a Zero Trust model. In this model, nothing is taken for granted and every request has to be verified. Service identity and authentication is perhaps the most fundamental piece of building Zero Trust environments.

![Spiffe-Spire](Pictures/spire-trust-domains.png)

If not done right and early, it could undermine your efforts to enable Zero Trust in your organization and introduce risk, complexity, and slow development velocity.

The Cloud Native Computing Foundation (CNCF) SPIFFE and SPIRE projects provide a universal service identity plane managing identity and trust within a zero trust security model. These projects provide a system for service to identify and authenticate themselves without the use of shared-secrets or network based security controls. Systems that adopt SPIFFE can easily and reliably mutually authenticate wherever they are running.

![Spiffe-Spire](Pictures/single-spire-server.png)

![Spiffe-Spire](Pictures/multiple-spire-servers.png)


This workshop will introduce SPIFFE and SPIRE concepts and demonstrate several simple use cases.


# Author: [Didier Lalli](mailto:didier.lalli@hpe.com)

## Handouts
You can freely copy these Jupyter Notebooks, including their output, in order to practice back at your office at your own pace, leveraging a local installation of Jupyter Notebook on your laptop.
- Install the Jupyter Notebook application from [here](https://jupyter.org/install) 
- A Beginners Guide is available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)


## Lab flow
{{ BRANDINGWOD }} Workshops-on-Demand are delivered through a central point that allows a portable, dynamic version of the lab guides. Rather than using standard PDF files which always end in copy / paste errors from the lab guide into the TS sessions, we leverage an infrastructure that uses a JupyterHub server on which all the different lab guides are stored in a notebook format (*.ipynb).

In a nutshell, a notebook works as follows:

• A notebook is a series of cells

• The notebook uses a kernel (visible in the upper right corner of the Notebook)

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

### Lab 1: SPIRE Fundamentals

* [Lab 1](1-WKSHP-SPIRE-Lab1.ipynb)


# Thank you!
![grommet.JPG](Pictures/grommet.JPG)


```bash

```
