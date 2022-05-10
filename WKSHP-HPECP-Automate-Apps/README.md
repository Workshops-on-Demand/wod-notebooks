![HPEDEVLogo](Pictures/hpe-dev-logo.png)

# Welcome to Hack Shack
[HPE Developer Community Team](https://hpedev.io)

# Speaker: [Chris Crawford](mailto:chris.crawford@hpe.com)


![Hack Shack](Pictures/hackshackdisco.png)



# Introduction to Automate Apps With the HPE Container Platform hands-on workshop
HPE Container Platform (HPECP) uses **container technology** to make it simpler and more cost-effective to deploy, run and manage both cloud native microservices enterprise workloads and non-cloud native monolithic stateful applications for machine learning, deep learning, and big data analytics use cases.

This workshop focuses on how developers can interact with HPECP programmatically through its REST API to accelerate their application development and deployment on containers. The workshops does not cover how to perform IT administrative tasks through the REST API.

You will start you off with some fundamental knowledge about how to interact with the HPE Container Platform programmatically through its REST API. As a tenant user, you will learn how to perform authentication, deploy cloud native stateless applications and non-cloud native distributed multi-node applications for AI/ML and data analytics, and interpret/respond to the status of your REST API calls. We will walk you through the process, step by step. By the end of the session, you'll be deploying a TensorFlow application framework and other simple applications. 
 

# Lab flow
HPE Developer Workshops-on-Demandare delivered through a central point that allows a portable, dynamic version of the lab guides. We are now leveraging a JupyterHub server on which all the different lab guides will be stored in a `Jupyter Notebook` format (*.ipynb). These Jupyter Notebooks are accessible from the internet for the event.

The notebooks can be downloaded on to your own laptop for further usage or editing. In order to use  them, you will need to install the Jupyter Notebook application, which is available [here](https://jupyter.org/install).
A Beginner's guide is also available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html).

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


Enjoy the lab! :-)

# Documentation and tools
The REST API documentation for HPE Container Platform is accessible from an HPE Container Platform deployment.

In the notebook, we'll primarily use `cURL` (Command-Line URL) to make REST API calls. cURL is the universal and well-appreciated utility in the Linux community. You will then use `kubectl` to make K8s API calls and interact with the Kubernetes cluster in the context of your tenant user account.

# Lab environment - A high level overview of the physical architecture of the HPE Container Platform deployment
This high-level architecture diagram depicts how you can interact programmatically with the HPE Container Platform. 
    

![HPECP-Architecture](Pictures/HPECP-Logical-diagram.jpg)
      

Our HPE Controller Platform deployment is comprised of a number of components:
1. The `Controller host` manages all the hosts that comprise the HPE Container Platform deployment.
2. The `Kubernetes (K8s) hosts` are under the direct control of the Controller host. These hosts can be grouped into one or more distinct Kubernetes clusters that run containerized applications.
3. The `Gateway host` acts as a proxy server that carries client requests like HPECP UI, REST API, K8s API (kubectl commands), to the HPE Container Platform controller, to one of the K8s clusters, or to the containerized application services running in one of the K8s clusters. Containerized application service endpoints are exposed outside the Kubernetes cluster to users via the gateway re-mapped ports. 
4. The `Authentication Proxy` handles user authentication and forwards authenticated K8s API traffic (kubectl commands) to the Kubernetes cluster master and returns any responses to the request back to the user.
5. The `HPE Data Fabric` (a MapR File System) is a storage provider for persistent volumes for the applications that require persistence of data. The default StorageClass is available out of the box from the HPE Data Fabric (MapR) using the HPE Container Storage Interface (CSI) driver for MapR.


# Lab 1: Deploy Applications via the HPECP REST API
In this intro, you will connect to the HPECP REST API endpoint and retrieve an authentication session token to be used for subsequent REST API requests and deploy the Splunk Application.

* [Lab 1](1-WKSHP-HPECP-Automate-Apps-with-HPECP.ipynb)


# Lab 2: Analyzing Data Sources in HPECP for Chargeback / Showback
In this lab, we will explore the various data sources provided by the HPECP to include how to interact with our Elastic stack and download usage reports.

* [Lab 2](2-WKSHP-HPECP-Charge-back-and-reporting.ipynb)

