![HPEDEVlogo](Pictures/hpe-dev-logo.png)

# Welcome to the HPE Developer Hack Shack
[HPE Developer Community Team](https://hpedev.io)

<p align="center">
  <img src="Pictures/hackshackdisco.png">
  
</p>

# HPE Developer Workshop



# Introduction to MLOPS101
In this workshop, using an example related predicting chances of diabetes amongst Pima Indians, you will be looking at the steps to build an **ML pipeline** that implements a basic end-to-end data science machine learning workflow process and that brings models to production. All of this in a single platform: **HPE Ezmeral ML Ops**.  

Technical Documentation: https://docs.containerplatform.hpe.com/53/reference/universal-concepts/About_HPE_Ezmeral_ML_Ops.html

Pipeline Components
•	CNCF certified Kubernetes cluster deployed on HPE Ezmeral Container Platform with multitenancy support and AD/LDAP integration.

•	ML Ops applications:

-	A local (lightweight) Jupyter Notebook cluster used by data scientists as a code sandbox to develop and test their models. Users can directly login to their local Jupyter Notebook server using their HPE Ezmeral ML Ops login credentials. 
-	A training cluster with large compute capacity (ideally with GPUs). Data scientists can submit the code they developed in their local Jupyter Notebook to a shared training cluster remotely. The training cluster offers a large scaled computing environment to data scientists to train their full ML models on, in a reasonable time, typically against a larger dataset.
-	An inferencing deployment engine cluster that exposes a secure and scalable RESTful API endpoint service that is used to serve the trained model as a prediction service.

•	Integrated collaboration tools. HPE Ezmeral ML Ops includes source control, project repository and model registry capabilities that organizations can utilize to standardize their ML workflows on a single platform and enhance collaboration among data science team and Operations team:

•	Version Control System (VCS) integrated into Jupyter Notebook ML Ops application. HPE Ezmeral ML Ops integrates with Git web-based version control systems such as GitHub or Bitbucket for implementation of source code control. Data scientists can maintain versioning of their model codes, commit codes to the VCS right from their Jupyter Notebook and collaborate with each other.

•	Central project repository used to share training data and trained models between containers and eliminating local copies of ML pipeline data and code. The NFS File System Mount (FSMount) features of HPE Ezmeral ML Ops is used to access the pre-integrated HPE Ezmeral Data Fabric for shared persistent container storage. The shared persistent container storage is mounted as an NFS File System mount point to all ML Ops application containers on a per-tenant basis. In our use case, by leveraging the pre-integrated HPE Ezmeral Data Fabric, HPE Ezmeral ML Ops makes it possible to store centrally and share the key data components (datasets, ML models and scoring scripts) across the ML Ops application components of the ML pipeline.

•	Model registry used to store metadata information and versions about the trained models within HPE Ezmeral ML Ops.

# Author: Terry Chiang (mailto:terry.chiang@hpe.com)

## Handouts
You can freely copy the Jupyter Notebooks, including their output, in order to practice back at your office at your own pace, leveraging a local installation of Jupyter Notebook on your laptop.
- You install the Jupyter Notebook application from [here](https://jupyter.org/install). 
- A Beginners Guide is also available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)


## Lab flow
HPE Developer Workshops-on-Demand are delivered through a central point that allows a portable, dynamic version of the lab guides. Rather than using standard PDF files which always end in copy / paste errors from the lab guide into the TS sessions, this year we decided to innovate and introduce a brand-new infrastructure. We will leverage a JupyterHub server on which all the different lab guides will be stored in a notebook format (*.ipynb).

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

### Lab 1: SetUp
Description: In this lab we will introduce and test the line magic functions that are apart of Ezmeral MLOps as well as populate our project repository with the necessary files.
* [Lab 1](1-WKSHP-Setup.ipynb)

### Lab 2: DataVisualization
Description: In this lab we will do some basic data visualization to see what kind of data we are working with.
* [Lab 2](2-WKSHP-DataVisualization.ipynb)

### Lab 3: Model Training
Description: In this lab we will take our data and train a couple of models using different algorithms and utilize our training cluster.
* [Lab 3](3-WKSHP-Model_Training.ipynb)

### Lab 4: Serving the Data
Description: In this lab we will :
* Register model
* Create model serving cluster
* Test inference

* [Lab 4](4-WKSHP-Serving.ipynb)

# Thank you!
![grommet.JPG](Pictures/grommet.JPG)
