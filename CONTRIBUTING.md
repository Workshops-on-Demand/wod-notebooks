This project is maintained by the [WoD Team](https://https://github.com/Workshops-on-Demand/wod-notebooks)

We accept contributions from the {{ BRANDING }} Community. 

Here is a simple How-to explaining how to contribute to the project with a new Notebook.

There are multiple cases possible depending on the type of workshop you wish to contribute for:

* Case1: Your workshop is self sufficient and does not require any Infra to run but the jupytherhub itself
    - In this case, simply follow the steps described below.
* Case2: Your workshop requires a VM to run aside of the jupyterhub.
    - In this case, additionnal scripts to support the workshop's vm setup, configuration, and customization. This means that on top of the current work of writing the workshop's notebooks, some additonal tasks will be needed and scripts to be written and added to the wod-backend repository. The current steps described below are also valid for the vm's management scripts in the wod-backend repo.

* Github Repository Cloning:

**Case 1**

From the following [Notebooks Repo](https://github.com/Workshops-on-Demand/wod-notebooks):
    -   Fork the repo to your personal repo
    -   Clone the repo with git clone and cd into it
    -	Create a branch for your workshop with git branch -b "branch Name". Name the branch after the the Workshop folder name (WKSHP-Example101)
    -   Add a folder for your stuff (WKSHP-Example101).
    -	Add a README.md that follows the same model as the one provided in other folders (WKSHP-API101 for example). Explain what the notebook is about, its dependencies if any.
    -	Add a LICENSE.md file by copying the one at the root of this repo (CC-By-SA 4.0)
    -	Add your notebook(s), make sure the link from your README.md works.
    -	Add the pictures from your notebooks in a Pictures folder.
    -	Finally edit the README.md file at the root of the repo to add your contribution to the list.
    -   Git add of the folder
    -   Git commit -m 'WOD WKSHP-Example101 Creation'
    -   Git push to your personal repo
    -   Submit a Pull Request
-	Then the [Notebooks Repo](https://github.com/Workshops-on-Demand/wod-notebooks) admin will check it and finally accept the request and merge it and delete the branch.

**Case2**
The overall process remains identical but:
From the following [wod-backend](https://github.com/Workshops-on-Demand/wod-backend):
    -   Fork the repo to your personal repo
    -   Clone the repo with git clone and cd into it
    -	Create a branch for your workshop with git branch -b "branch Name". Name the branch after the the Workshop folder name (WKSHP-Example101)
    -   cd in the scripts folder
    -	Add the following scripts:
        -   Cleanup-WKSHP-Example101
        -   Create-WKSHP-Example101
        -   Reset-WKSHP-Example101
        -   Setup-WKSHP-Example101
    -   If an appliance is requiered:
        -   One will need to add a setup-appliance script in the Ansible folder and append some variables in the Ansible/Group_vars/wod-backend file
        -   If the workshop is not meant to be a public one, then achieve the same steps with your wod-backend private repo.
    -   Git add of the folder
    -   Git commit -m 'WOD WKSHP-Example101 Scripts Creation'
    -   Git push to your personal repo
    -   Submit a Pull Request
-	Then the [wod-backend](https://github.com/Workshops-on-Demand/wod-backend) admin will check it and finally accept the request and merge it and delete the branch.

We will do our best to review and respond as quickly as possible.

Thanks,

WoD Team
