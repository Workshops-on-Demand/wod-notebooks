![HPEDEVlogo](Pictures/hpe-dev-logo.png)       ![GreenLake](Pictures/greenlake-hero.jpg)

# Welcome to the HPE Developer Hack Shack
Powered by [HPE Developer Community Team](https://hpedev.io)

<p align="center">
  <img src="Pictures/hackshackdisco.png">
  
</p>

# HPE Developer Workshops-on-Demand

# Introduction to HPE GreenLake Private Cloud Virtual Machines API
HPE GreenLake Central is an advanced software-as-a-service platform that provides you with a consistent cloud experience for all your applications and data—on-premises or off-premises. It provides you with insights and controls to manage your hybrid IT estate, complementing your use of public clouds and data centers. HPE GreenLake Central gives you the ability to choose where and how to place your workloads and data, and—through the services you purchase—enables you to monitor security, compliance, capacity, resource utilization, and costs.

In HPE GreenLake Central, you can do the following:

- View and manage the services available to you in your HPE GreenLake environment.

Services you use through HPE GreenLake Central appear as widgets on the HPE GreenLake Central Dashboard.

- Request and try services that have been offered to you to evaluate through HPE GreenLake Central.

- With help from your HPE representative, manage your users and their access to resources in your environment, including access to other tools that are part of the services you purchase or use on a trial basis.

In this workshop we’ll go through some basic usage of the Virtual Machine As a Service API that IT OPS / DEV OPS would use to interact programmatically with their resources. You will see through the basics of the authentification mechanisms. Then you'll get a chance to list a few of these resources available in your tenant. Deploying an instance is a simple but efficient example one needs to go through too along with all the different actions related to it (stop, start, restart, backup...). You will also run some tasks and finally get your hands on a simple blueprint deployment. This workshop does not cover all the features of the HPE GreenLake VMAAS offering. It simply offers you the possiibility to tet just a few of them.

# Authors:[Frederic Passeron](mailto:frederic.passeron@hpe.com)    &     [Vinnarasu Ganesan](mailto:vinnarasu.ganesan@hpe.com)

## Handouts
You can freely copy the Jupyter Notebooks, including their output, in order to practice back at your office at your own pace, leveraging a local installation of Jupyter Notebook on your laptop.
- You install the Jupyter Notebook application from [here](https://jupyter.org/install). 
- A Beginners Guide is also available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)


## Lab flow
Workshop-on-Demand Workshops are delivered through a central point that allows a portable, dynamic version of the lab guides. Rather than using standard PDF files which always end in copy / paste errors from the lab guide into the TS sessions, this year we decided to innovate and introduce a brand-new infrastructure. We will leverage a JupyterHub server on which all the different lab guides will be stored in a notebook format (*.ipynb).

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

### Lab 1: Authentification
Description: In this section, we’ll go through some of the necessary steps to retrieve the API Token necessary for authewntification. Then we will look some of the components used to build, deploy a new instance.
* [Lab 1](1-WKSHP-VMAAS-Authentification.ipynb)

### Lab 2: Instance Creation
Description: In this section, we’ll go through some of basics actions to create an instance and then manage it (stop / start / snpashot, etc...)
* [Lab 2](2-WKSHP-WKSHP-VMAAS-Instance.ipynb)

### Lab 3: Blueprint deployment
Description: In this section, we’ll go through a simple yet relevant blueprint deployment.
* [Lab 3](3-WKSHP-WKSHP-VMAAS-Blueprint.ipynb)


# Thank you!
![grommet.JPG](Pictures/grommet.JPG)


```python

```


```python

```
