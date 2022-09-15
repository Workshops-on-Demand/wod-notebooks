![HPEDEVLogo](Pictures/hpe-dev-logo.png)

# Welcome to Hack Shack
[HPE Developer Community Team](https://hpedev.io)

# HPE Developer Workshop



# Build a house on the lake

*Version: HPE Ezmeral Runtime Enterprise 5.4+ with HPE Ezmeral ML Ops, Persistent Storage from HPE Ezmeral Data Fabric version 6.2

Know little to nothing about Apache Spark? Maybe you’ve heard of the terms Data Lake,Data Warehouse, Delta Lake, and Lakehouse? Yes or no, you’re perfectly prepared to step up, put on your Data Driven Developer hat and create your first Lakehouse architecture! Ingest data from a Data Lake and convert it to Apache Spark Delta Lake format. Then perform SQL queries on it, create streams of data, and verify ACID compliance! Within an hour you’ll be a ready to build a house on a lake! Yay! Lets go! :-)

# Authors: [Don Wake](mailto:donald.wake@hpe.com)
<img src="Pictures/lakehouse.png" align="center">

## Handouts
HPE Developer Workshops-on-Demand are delivered through a central point that allows a portable, dynamic version of the lab guides. Rather than using standard PDF files which always end in copy / paste errors from the lab guide into the TS sessions, this year we decided to innovate and introduce a brand-new infrastructure. We will leverage a JupyterHub server on which all the different lab guides will be stored in a notebook format (*.ipynb).

You can freely copy the Jupyter Notebooks, including their output, in order to practice back at your office at your own pace, leveraging a local installation of Jupyter Notebook on your laptop.
- You install the Jupyter Notebook application from [here](https://jupyter.org/install). 
- A Beginners Guide is also available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)

## A quick look at Jupyter Notebook
Jupyter Notebook is an open source solution for interactive documents that are commonly used to hold code for ML/DL models. 
A Notebook consists of cells. A cell can be a markdown cell (contains comments, text, images) or a code cell. 

To execute code within the Notebook, you run each cell in turn by clicking on the ***Play button*** in the menu bar of the Notebook.

> **Note:**  When you see a [*] next to the action it means your execution step is busy working within the notebook. When you see a digit number, it means the execution of the step is completed.  

![QickLookNotebook](Pictures/Quick-look-Notebook.png)


Enjoy the labs ! :-)


# Our Lakehouse Build Plan (Lab flow)
<img src="Pictures/your-are-here.png" height="60%" width="60%" align="right">

### Lab 1: Authenticate as tenant user to HPE Ezmeral ML Ops using REST API calls
In this first lab, you will connect to the HPE Ezmeral Runtime Enterprise platform.  We have created a Kubernetes cluster for you and further we have created a special Kubernetes namespace or "tenant" called deltalake. In Lab 1 you will use API calls to HPE Ezmeral Runtime Enterprise to retrieve an authentication session token. This token is then used for fetching the KubeConfig file you will need to interact with the Kubernetes cluster available for your tenant.

* [Lab 1](1-WKSHP-DeltaLake-Auth-Get-Kubeconfig-v2.ipynb)


### Lab 2: Deploy a local Jupyter Notebook sandbox on HPE Ezmeral ML Ops and access it
In this lab, you will deploy an HPE Ezmeral Runtime Enterprise managed Jupyter Notebook cluster. Data scientists typically use this type of Jupyter Notebook as a code sandbox for many data engineering and machine learning related tasks. It is important to understand that there are two different Jupyter Noteboook servers being used in this workshop.  In Lab 0, Lab 1 and Lab 2 you are running Jupyter Notebook cells to get setup to run Lab 3. In Lab 2 you are executing API calls to the HPE Ezmeral Runtime Enterprise platform so that you can launch a containerized kubernetes application managed by HPE Ezmeral Runtime Enterprise. Once that cluster is up and running on a completely different set of servers, you will click on the Web URL that you generate in Lab 2, to access the application's service endpoint.

* [Lab 2](2-WKSHP-DeltaLake-Deploy-Notebook-w-ml-v2.ipynb)

### Lab 3: Run PySpark code in our HPE Ezmeral ML Ops managed Jupyter Notebook
In Lab 3 we are using an application called "Jupyter Notebook with ML Toolkits". This application was accessed via a Web URL or service endpoint, being managed by HPE Ezmeral Runtime Enterprise. This application is pre-built and configured for you in the "Notebooks" section of your ML Ops Tenant.  The application was built by HPE using another integrated tool called KubeDirector to simplify stateful application deployment in Kubernetes.  Learn more [here](https://kubedirector.io) Lab 3 is entirely devoted to running PySpark code with time saving integrated tools such as custom magic commands and the integration of the HPE Ezmeral Runtime Enterprise DataTap feature.  DataTap literally allows you to "Tap into" an existing HDFS or MAPRFS based Data Lake and utilize the Apache Spark Delta Lake framework to change your Data Lake into a Lakehouse.


### Lab 4 - Conclusion
Review the Workshop and conclude.

>**Note:** _This workshop is not intended to teach you about a full Machine Learning Pipeline, however it does showcase how 
an HPE Ezmeral ML Ops tenant can be used to create a Delta Lake based application using a preconfigured
kubernetes application called "Jupyter Notebooks with ML Toolkits" ._

## Technical Documentation
* Learn about HPE Ezmeral Runtime Enterprise 5.4 managed Jupyter Notebooks [here](https://docs.containerplatform.hpe.com/54/reference/kubernetes/using-kubernetes/ai-ml-functionality/notebooks/notebooks.html). 

* Learn about HPE Ezmeral Runtime Enterprise 5.4 provided custom Jupyter Notebook "Magic" functions here [here](https://docs.containerplatform.hpe.com/54/reference/kubernetes/using-kubernetes/ai-ml-functionality/notebooks/Kubernetes_Notebook_Magic_Functions.html)

* Learn how to connect kubernetes apps to your Data Lake using DataTap [here](https://docs.containerplatform.hpe.com/54/reference/universal-concepts/copy_kubernetes-tenant-project-administration-About_DataTaps.html)

* Learn about using HPE Ezmeral Data Fabric as the ultimate Global Lakehouse [here](https://docs.datafabric.hpe.com/)


# Thank you!
![grommet.JPG](Pictures/grommet.JPG)



```python

```
