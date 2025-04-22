# Programming & Scripting Project 2025

## *Investigating the Iris Dataset*

![Alt text](images/iris-species.png)


## Overview 🌸

This repository contains an introductory investigation into the iris dataset completed as part of the assessment requirements for the *Programming and Scripting* module at Atlantic Technological University – Galway.

As a beginner to both programming and data analytics, the primary aim of this project was to build foundational skills in data analytics using Python, by preforming an investigation into the iris dataset.

The analysis begins with exploratory data analysis (EDA) to examine the structure and statistical properties of the dataset. Visualizations are employed to illustrate patterns, relationships, and class distributions within the data. Finally, simple machine learning algorithms are implemented to classify iris species based on the dataset’s features.

Through this project, I have gained practical experience in working with real-world data, using tools and libraries such as pandas, matplotlib, seaborn, and scikit-learn. The work reflects a progression in my understanding of core data analytics concepts and programming practices.

Author: Niamh Hogan

## About this Repository 🌸

This repository is comprised of the following files and folders:

* A **README** file containing a brief summary of the iris dataset, 
* An **images** folder containing .png files of
* A Jupyter Notebook titled: **investigations.ipynb**  
  - briefly discuss sections
* An **analysis.py** file which includes only the code.


## Summary of the Iris Dataset 🌸

The Iris dataset is a well-known multivariate dataset comprising 150 observations, evenly distributed across three species of the Iris flower: Iris setosa, Iris versicolor, and Iris virginica, with 50 instances representing each class. Each sample is described by four continuous numerical features: sepal length, sepal width, petal length, and petal width, all measured in centimeters, thereby ensuring consistency in measurement units. ([GeeksforGeeks, 2024](https://www.geeksforgeeks.org/iris-dataset/))

In 1936, Ronald Fisher introduced the Iris dataset in his paper *The Use of Multiple Measurements in Taxonomic Problems*, aiming to demonstrate the application of statistical techniques to classification challenges. Fisher posited that distinct morphological characteristics among Iris species, specifically measurements of sepal and petal length and width, could be leveraged to infer species membership. Utilizing a combination of these four features, he formulated a linear discriminant analysis (LDA) model capable of differentiating among the species. Furthermore, he suggested that the species of an unclassified iris flower could be predicted using the statistical patterns derived from the dataset. ([Fisher, 1936](https://www.semanticscholar.org/paper/THE-USE-OF-MULTIPLE-MEASUREMENTS-IN-TAXONOMIC-Fisher/ab21376e43ac90a4eafd14f0f02a0c87502b6bbf))

The Iris dataset continues to serve as a foundational resource in the fields of data analysis, machine learning, and pattern recognition, due to several notable characteristics ([Brownlee, 2016](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)):  

  - The dataset is both complete and balanced, containing no missing values and featuring an equal number of observations for each class.

  - All four features — sepal length, sepal width, petal length, and petal width are measured in consistent units (centimeters), ensuring standardization in data representation.

  - The Iris setosa species is linearly separable from the other two species, facilitating clear differentiation. Although Iris versicolor and Iris virginica exhibit some degree of overlap, they can still be effectively distinguished using specific feature combinations. This inherent structure makes the dataset particularly suited for introductory studies in classification and highlights its substantial predictive capabilities.

## Dependencies 🌸

  - Python==3.12.7  
  - Matplotlib  
  - seaborn  
  - pandas  
  - NumPy  

## Environment Setup 🌸

## How to Download Repository 🌸

## How to Run the Project 🌸


## References 🌸

Brownlee, (2016) https://machinelearningmastery.com/machine-learning-in-python-step-by-step/  

Fisher, R.A. (1936). THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC PROBLEMS. Annals of Human Genetics, 7, 179-188.

GeeksforGeeks. (2024). Iris dataset. GeeksforGeeks. https://www.geeksforgeeks.org/iris-dataset/