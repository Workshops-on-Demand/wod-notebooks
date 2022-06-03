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

To complete the workshop, you need to go through the different labs that make up the workshop. Labs are made of cells that needs to be executed. The quiz is related to the workshop you have selected. There are only a few questions to answer (up to 3 maximum).![HPEDEVlogo](Pictures/hpe-dev-logo.png)


# Getting Started with Determined, the Open-Source Deep Learning Training Platform

*Version: open source Determined 0.17.9+*

Determined AI (or Determined) is an open source platform built to accelerate deep learning (DL) experimentation for data science teams. These teams can use Determined to build, train, and optimize their deep learning models. Determined provides the tools for accelerating experiments, such as distributing training and automatic model tuning, with hyperparameter search, also known as hyperparameter optimization (HPO). 

In this workshop, you will learn about some fundamental features and terminology of Determined. You will take a specific deep learning model and walk through how to interact with the Determined system to train the DL model and visualize the result of the training process. You will experience how Determined makes it easy for ML engineers and data scientists to train deep learning models on one or more GPUs to accelerate training processes, and how it simplifies hyperparameter optimization (HPO) to improve model accuracy and find the best version of a model. 

>**Note:** _This workshop is not intended to teach you about AI/ML/DL or how to "port" your deep learning model to Determined. It is intended to give a use case for data science and ML engineers to get started with Determined and some of its fundamental concepts and features. The DL model used in this hands-on workshop is abbreviated from [the popular iris classification example](https://github.com/determined-ai/determined/tree/master/examples/computer_vision/iris_tf_keras)._


# Authors: [Denis Choukroun](mailto:denis.choukroun@hpe.com)

<p align="center">
  <img src="Pictures/hackshackdisco.png">
  
</p>

## Handouts
HPE Developer Workshops-on-Demand are delivered through a central point that allows a portable, dynamic version of the lab guides. Rather than using standard PDF files that always end in copy / paste errors from the lab guide into the TS sessions, we leverage an infrastructure that uses a JupyterHub server on which all the different lab guides are stored in a notebook format (*.ipynb).

You can freely copy the Jupyter Notebooks, including their output, in order to practice back at your office at your own pace, leveraging a local installation of Jupyter Notebook on your laptop.
- Install the Jupyter Notebook application from [here](https://jupyter.org/install) 
- A Beginners Guide is available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)

## A quick look at Jupyter Notebook
Jupyter Notebook is an open source solution for interactive documents that are commonly used to hold code for ML/DL models. 
A notebook consists of cells. A cell can be either a markdown cell (contains comments, text, images) or a code cell. 

To execute code within a notebook, you run each cell in turn by clicking on the ***Play button*** in the menu bar of the notebook.

> **Note:**  When you see an [*] next to the action, it means your execution step is busy working within the notebook. When you see a digit number, it means the execution of the step is completed.  

![QickLookNotebook](Pictures/Quick-look-Notebook.png)

Enjoy the labs ! :-)


## Learn more

Visit the technical documentation [here](https://docs.determined.ai/latest/) for how to get started with Determined, and check out the [Determined GitHub repository](https://github.com/determined-ai/determined). 

Be sure to also join the [Determined Community Slack group]( https://join.slack.com/t/determined-community/shared_invite/zt-cnj7802v-KcVbaUrIzQOwmkmY7gP0Ew). 

# Lab environment

Determined is open source and it can be deployed on-premises in your data center, on any hardware, on Kubernetes, or in public clouds. 

For this workshop, the Determined system consists of Determined software deployed as an on-premises cluster, with GPUs, in a Kubernetes cluster managed by [HPE Ezmeral Runtime Enterprise](https://developer.hpe.com/platform/hpe-ezmeral-runtime/home/). You are all sharing the Kubernetes cluster resources with other participants.

The diagram below depicts the components that make the Determined system on the Kubernetes cluster. 

<img src="Pictures/DetAI-Lab-Environment-architecture.png" height="382" width="700" align="right">

The Determined system consists of:
* A **Master**, which is attached to a **PostgreSQL** database. The Master and Database run as containers, each within a Kubernetes POD, in the worker nodes of the Kubernetes cluster. 
    * The Master hosts the interfaces service endpoint that clients use to communicate with the Determined system, through a CLI, WebUI, and APIs. 
    * The Master brings up PODs on the Kubernetes worker nodes to run tasks on demand; for example, the model training tasks and auxiliary tasks such as TensorBoard and JupyterLab Notebook.
    * As training tasks execute, the Master remains in communication with the training tasks PODs and saves training model metadata (for example the training & validation metrics received from the training tasks), as well as the state of the tasks in the PostgreSQL database for model experiment tracking and analysis.  
* The Ingress Gateway makes the Master's interfaces service endpoints reachable from outside the Kubernetes cluster. 
* The Distributed File System of the pre-integrated HPE Ezmeral Data Fabric is leveraged to provide both _persistent storage_ for containerized application such as the Determined PostgreSQL database for model experiments tracking and a _shared file system_ mounted on each Kubernetes worker host. The shared file system is needed by the Determined system to store the ***model datasets*** on which the model will be trained by the training tasks. The shared file system is also needed to store the ***model artifacts*** (model definition files, model code) and the training task's ***checkpoints***, which are saved versions of validated models that data science teams can access later for testing and analysis and make available to a deployment or serving solution, such as Seldon core.

# Lab workflow

## Lab 1: Learning the base principles of Determined
In this first lab, you will be introduced to Determined system components and some of its important concepts and terminology. You will learn how to interact with **Determined** system deployed on Kubernetes using the Determined CLI. You will launch your first experiment (i.e. training task) to train a deep learning model with Determined, monitor and visualize training task progress and gather the metrics of the training for analyzing results using Determined WebUI and the integrated TensorBoard. Finally, you'll launch a JupyterLab server task from within Determined system, load your trained model, and test it by making predictions.

* [Lab 1](1-WKSHP-DET-AI-101-Getting-started-DetCLI.ipynb)

## Labs 2: Distributed training with Determined
For this part of the lab, you will learn how to create an experiment that trains a single instance of the model with multiple GPUs, a process known as **Distributed Training**, without requiring any model code changes.

* [Lab 2](2-WKSHP-DET-AI-101-Getting-started-Dist-Training.ipynb)

## Labs 3: Hyperparameter optimization with Determined
For this part of the lab, you will explore how Determined's automatic model tuning with hyperparameter search, also known as hyperparameter optimization (HPO), can help improve the model accuracy and let you find the best combination of hyperparameters that yields the best version of your model, without requiring any model code changes. 

* [Lab 3](3-WKSHP-DET-AI-101-Getting-started-HPO.ipynb)

## Join the HPE Developer Community
![QRCode](Pictures/QRCode-HPEDEV.png)

# Thank you!
![grommet.JPG](Pictures/grommet.jpg)


```python

```
