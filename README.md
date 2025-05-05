# Programming & Scripting Project 2025

## *Investigating the Iris Dataset* 

![Alt text](images/iris-species.png)


## Overview 🌱


This repository contains an introductory investigation into the iris dataset completed as part of the assessment requirements for the *Programming and Scripting* module at Atlantic Technological University – Galway.

As a beginner to both programming and data analytics, the primary aim of this project was to build foundational skills in data analytics using Python, by preforming an investigation into the iris dataset.

I began my analysis with exploratory data analysis (EDA) to examine the structure, health and statistical properties of the dataset.

--

Through this project, I have gained practical experience in working with real-world data, using tools and libraries such as pandas, matplotlib, seaborn, and scikit-learn. The work reflects a progression in my understanding of core data analytics concepts and programming practices.

Author: Niamh Hogan

## About this Repository 🌸

This repository is comprised of the following files and folders:

* A **.gitignore** file which contains all the files/folders to be ignored by Git in the repository.
* A **README** file containing a brief summary of the iris dataset, 
* An **images** folder containing .png files of
* A Jupyter Notebook titled: **investigations.ipynb**  
  - briefly discuss sections
* An **analysis.py** file which includes only the code.


## Summary of the Iris Dataset 🌸

The Iris dataset is a well-known multivariate dataset comprising 150 observations, evenly distributed across three species of the Iris flower: Setosa, Versicolor, and Virginica, with 50 instances representing each class. Each sample is described by four continuous numerical features: sepal length, sepal width, petal length, and petal width, all measured in centimeters, thereby ensuring consistency in measurement units. ([GeeksforGeeks, 2024](https://www.geeksforgeeks.org/iris-dataset/))

In 1936, Ronald Fisher introduced the Iris dataset in his paper *The Use of Multiple Measurements in Taxonomic Problems*, aiming to demonstrate the application of statistical techniques to classification challenges. Fisher posited that distinct morphological characteristics among Iris species, specifically measurements of sepal and petal length and width, could be leveraged to infer species membership. Utilizing a combination of these four features, he formulated a linear discriminant analysis (LDA) model capable of differentiating among the species. Furthermore, he suggested that the species of an unclassified iris flower could be predicted using the statistical patterns derived from the dataset. ([Fisher, 1936](https://www.semanticscholar.org/paper/THE-USE-OF-MULTIPLE-MEASUREMENTS-IN-TAXONOMIC-Fisher/ab21376e43ac90a4eafd14f0f02a0c87502b6bbf))

The Iris dataset continues to serve as a foundational resource in the fields of data analysis, machine learning, and pattern recognition, due to several notable characteristics ([Brownlee, 2016](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)):  

  - The dataset is both complete and balanced, containing no missing values and featuring an equal number of observations for each class.

  - All four features — sepal length, sepal width, petal length, and petal width are measured in consistent units (centimeters), ensuring standardization in data representation.

  - The Iris setosa species is linearly separable from the other two species, facilitating clear differentiation. Versicolor and Virginica exhibit some degree of overlap. However, they can still be effectively distinguished using specific feature combinations. This inherent structure makes the dataset particularly suited for introductory studies in classification and highlights its substantial predictive capabilities.

## Dependencies 🌸

**See tasks.ipynb for further information on the following libraries** 
- Python==3.12.7  
- Matplotlib.pyplot==3.9.2 
- seaborn==0.13.2  
- pandas==2.2.2
- NumPy==1.26.4
- scikit-learn==1.5.1

## Technologies 🌸  
- Python
- Anaconda
- Git
- GitHub
- Jupyter Notebooks
- Visual Studio Code

## Environment Setup 🌸  

For downloading and running the repository locally download the following:

**Git**

Download the latest version of Git at:
https://git-scm.com/downloads

**GitHub**

Create a free GitHub account at:
https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home

**Anaconda**

I recommend using Anaconda as it comes bundled with Python, Jupyter Notebooks & the Python libraries used in this repository.
Install Anaconda using the following steps:

  1. Download Anaconda for free from:  
  https://www.anaconda.com/download  
  2. Open the downloaded file & press next, next
  3. When the advanced options appear check the following boxes:
  - Add to PATH environment variable
  - Make this version your default Python

**Visual Studio Code**

Download Visual Studio Code at:  
https://code.visualstudio.com/Download

  - Install Python & Jupyter extensions in VS Code

## How to Download Repository 🌸  

You can clone this repository to VS Code using the following steps:

  1. Copy the repositories URL from GitHub:  
  https://github.com/NibnabCodes/pands_project
  2. Create a folder in VS Code of where you want to store the cloned repository
  3. Open new terminal in VS Code & input following:
  - git clone PASTED.URL - To clone repository
  - git config pull.rebase false - Set pull mode to merge
  - git pull - To pull the content of the repository

The repository should now be accessible in VS Code & ready to execute.

## How to Run the Project 🌸  
  1. Open repository folder in VS Code
  2. Open .ipynb file
  3. In the top right-hand corner click "select kernel"
  4. select Python environment
  5. To execute the cells to run the code within the notebook, select "Run All" or run the cells one by one by clicking "▶️ Execute cell" on the top left-hand corner of the cell


## References 🌸

*See **investigations.ipynb** for references used to complete project*

Brownlee, J. (2016). Machine learning in Python: Step-by-step tutorial. Machine Learning Mastery. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

Fisher, R. A. (1936). The use of multiple measurements in taxonomic problems. Annals of Human Genetics, 7(2), 179–188. https://doi.org/10.1111/j.1469-1809.1936.tb02137.x

GeeksforGeeks. (2024). Iris dataset. GeeksforGeeks. https://www.geeksforgeeks.org/iris-dataset/