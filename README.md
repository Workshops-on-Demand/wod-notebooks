# wod-notebooks
This project is the public notebook repo part of our Workshop-on-Demand setup. You can test them live at https://hackshack.hpedev.io/workshops

## The repo contains a serie of public workshops.
A public workshop is a workshop that is based on open source technology. It does not require proprietary technology. As an example, API101 only requires a publicly available API to work. On the other side, a workshop requiring HPE OneView API endpoint can not be considered as public as it needs an HPE Propriatery technology to run.
A workshop is built up in its own directory: 

API101 Workshop example: WKSHP-API101/

The directory must be named with the prefix WKSHP- followed by some workshop name.

A workshop directory contains the following.

A series of Jupyter Notebooks: 

The naming convention requires a digit followed by WKSHP, then lab part name. It also includes details on notebooks technology and how to use them.

* 0-ReadMeFirst.ipynb => This notebook contains generic infos on the workshop. It introduces the subjects, the concepts as well as the flow of the workshop. A workshop can be made of several parts. 
* 1-WKSHP-REST_API_Basics.ipynb => Lab 1 of the Workshop. There could be multiple labs and part number would increment.
* 2-WKSHP-Conclusion.ipynb => Conclusion of the workshop summarizing the different steps achieved.

The workshop directory also contain a Pictures folder in which relevant pictures needed by the notebooks are located.

The workshop directory may contain additional folders required by the workshop.

Finally, it should contain an auto generated readme.md file based on the 0-ReadMeFirst.ipynb notebook.

Here is a list of the current public available Workshops:
|   Name      | Description |  Backend needed |
| :---        |  :---   | :---   | 
|      |       |      | 
| WKSHP-API101  | Basic Concepts on an API        | No |
| WKSHP-Concourse1011  | Basic Concepts on CICD        |  Yes |
| WKSHP-Docker101  | Basic Concepts on Docker Containers        |  Yes |
| WKSHP-GIT101  | Basic Concepts on GIT        | No |
| WKSHP-Grommet  | Basic Concepts on Grommet        |  No |
| WKSHP-Jupyter-Notebooks101  | Basic Concepts on Jupyter Notebooks        | No |
| WKSHP-ML101 | Basic Concepts on an Machine Learning       | No |
| WKSHP-Python101  | Basic Concepts on Python Programming Language        | No |
| WKSHP-RUST101  | Basic Concepts on RUST Programming Language        | No |
| WKSHP-SPIFFE-SPIRE-101  | Basic Concepts on SPIFFE-SPIRE        | No |
| WKSHP-Spark01  | Basic Concepts on Apache Spark         | Yes |
| WKSHP-StackStorm101 | Basic Concepts on StackStorm automation framework       | Yes |
| WKSHP-Ansible101  | Basic Concepts on Ansible        | Yes |
| WKSHP-DataVisu101  | Basic Concepts on Data Visualization        | Yes |
| WKSHP-LLM101  | Basic Concepts on Large Language Model      | Yes |


A workshop may require some separate scripts. These scripts would be needed to:
* Build up a generic appliance required by the workshop,
* Setup the appliance to the needs of the workshop,
* Configure the appliance at the deployment phase of the workshop,
* Reset the appliance if needed by the workshop.

The required scripts are located in the wod-backend repo under the scripts folder.
