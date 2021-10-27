Welcome to Focus Shack!
In this workshop, using an example related predicting chances of diabetes amongst Pima Indians, you will be looking at the steps to build an **ML pipeline** that implements a basic end-to-end data science machine learning workflow process and that brings models to production. All of this in a single platform: **HPE Ezmeral ML Ops**.  

Technical Documentation: https://docs.containerplatform.hpe.com/53/reference/universal-concepts/About_HPE_Ezmeral_ML_Ops.html

Prerequisites
Before going on please have the following set up on your installation of the Ezmeral Container Platform 
    1. Kubernetes MLOps tenant 
    2. KubeDirector Training Cluster (https://docs.containerplatform.hpe.com/53/reference/epic/working-with-ai-ml/training/Creating_A_New_Training_Cluster.html)
    3. KubeDirector Notebook attached to the training cluster (https://docs.containerplatform.hpe.com/53/reference/epic/working-with-ai-ml/notebooks/Creating_A_New_Notebook_Cluster.html)
    
NOTE TO SELF (Terry): Should we add steps to create the notebook and training clusters?
    
Make sure you have the following files 
Code 
        -> 0-ReadmeFirst.txt
        -> 1-SetUp.ipynb
        -> 2-DataVisualization.ipynb
        -> 3-Modeling_Training.ipynb
        -> 4-Serving.ipynb
        -> Diabetes_Scoring.py
	
Data
        -> pima-indians-diabetes.csv





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

Please login to your notebook and upload the contents of the lab to your notebook. 
