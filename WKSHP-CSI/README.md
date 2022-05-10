![HPEDEVlogo](Pictures/hpe-dev-logo.png)

# Welcome to the HPE Developer Hack Shack

[HPE Developer Community Team](https://hpedev.io)

# Creator: [Michael Mattsson](mailto:michael.mattsson@hpe.com)

Find me on [Twitter](https://twitter.com/datamattsson), [LinkedIn](https://www.linkedin.com/in/michael.mattsson), [Blog](https://datamattsson.io) 

<p align="center">
  <img src="Pictures/hackshackdisco.png">
</p>

# Using the Container Storage Interface (CSI) with HPE Ezmeral Container Platform

In this workshop, we’ll go through some of the basic primitives that CSI introduces to Kubernetes as part of the HPE Ezmeral Container Platform. We will also revisit some of the staple objects such as `StorageClasses`, `PersistentVolumeClaims` and `PersistentVolumes`. 

A recorded instructor led session of the CSI workshop is available in the [HPE DEV Workshop-on-Demand](https://hackshack.hpedev.io/replays/2).

## JupyterHub

You can freely copy the Jupyter Notebooks, including their output, in order to practice back at your office at your own pace, leveraging a local installation of Jupyter Notebook on your laptop.

- You can install the Jupyter Notebook application from [here](https://jupyter.org/install). 
- A Beginners Guide is also available [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)

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


Enjoy the labs! :-)

## Workflow

Each lab is self-contained and maybe completed in any order. Just make sure to download your KUBECONFIG before you begin (Lab 0).

### Lab 0: Retrieve your KUBECONFIG

The first step is to retrieve your KUBECONFIG file. If, for any reason, you lose authentication for the remainder of the labs, rerun the KUBECONFIG notebook.

* [KUBECONFIG](Z-WKSHP-CSI-KUBECONFIG.ipynb)

### Lab 1: Persistent Storage Basics

In Lab 1, you will learn about `StorageClasses`, `PersistentVolumeClaims` and `PersistentVolumes`. In it, you will use different `volumeMode` attributes and resize your `PersistentVolumeClaim`.

* [Lab 1: Persistent Storage Basics](1-WKSHP-CSI-Basics.ipynb)

### Lab 2: Snapshots and Clones

In Lab 2, you will utilize `VolumeSnapshotClasses` to create `VolumeSnapshots` and use them to restore data into new `PersistentVolumeClaims`. This lab also covers how to use an existing `PersistentVolumeClaim` as a `dataSource`.

* [Lab 2: Snapshots and Clones](2-WKSHP-CSI-DataManagement.ipynb)

### Lab 3: Ephemeral Inline Volumes

Need temporary space that `emptyDir` or `hostPath` simply can't give you? Ephemeral Inline Volumes is the tool for the job. In Lab 3, we will show you how to use this tool.

* [Lab 3: Ephemeral Inline Volumes](3-WKSHP-CSI-Inline.ipynb)

### Lab 4 (Optional): Non-portable HPE CSI Driver Capabilities

CSI leaves a lot of headroom to innovate. Check out what we can do specifically with the HPE CSI Driver for Kubernetes in Lab 4.

* [Lab 4: Non-portable HPE CSI Driver Capabilities](4-WKSHP-CSI-HPE.ipynb)

# Conclusion

You are done! Let's [conclude this workshop](5-WKSHP-CSI-Conclusion.ipynb)!
