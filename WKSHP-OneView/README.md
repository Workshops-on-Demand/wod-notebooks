![HPEDEVlogo](Pictures/hpe-dev-logo.png)

# Welcome to the HPE Developer Hack Shack
[HPE Developer Community Team](https://hpedev.io)

<p align="center">
  <img src="Pictures/hackshackdisco.png">
  
</p>

# Workshops on Demand

# OneView API Basics 
![](Pictures/OneViewLogo.png)


# Author: [Vincent Berger](mailto:vincent.berger@hpe.com)


For this OneView interactive demo-lab, we will look at both PowerShell and Python code working with the OneView API, as well as some raw API calls using curl. Beginners and experts are welcome.

## Introduction to the HPE OneView API
REST (Representational State Transfer) is a style of API that uses basic Create, Read, Update and Delete (CRUD) operations that are performed on resources using HTTP POST, GET, PUT, PATCH and DELETE requests. To learn more about general REST concepts, see
http://en.wikipedia.org/wiki/Representational_state_transfer  
HPE OneView has a resource-oriented architecture that provides a uniform REST interface. Every resource has one Uniform Resource Identifier (URI) and represents a physical device or logical construct, and may be manipulated using REST APIs. To view the list of resources, see the [HPE OneView API Reference](https://techlibrary.hpe.com/docs/enterprise/servers/oneview5.0/cicf-api/en/index.html#about)  

# Lab Flow
HPE Developer Workshops-on-Demand are delivered through a central point that allows a portable, dynamic version of the lab guides. We are now leveraging a jupyterhub server on which all the different labs guides will be stored in a Notebook format (*.ipynb). These Notebooks are accessible from the internet for the event.

Besides, the notebooks can be downloaded on to your own laptop for further usage or edition. In order to use  them, you will need to install the jupyter notebook application available [here](https://jupyter.org/install).
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

# Lab 1: First steps with the API and PowerShell
In this section, we will use PowerShell to cover the basics of the HPE OneView API

* [Lab 1](1-WKSHP-OVAPIPowerShell.ipynb)

# Lab 2: Using Python and the OneView API
We will switch to Python to do what we previously did with PowerShell

* [Lab 2](2-WKSHP-OVAPIPython.ipynb)


# Thank You!
![grommet.JPG](Pictures/grommet.JPG)

