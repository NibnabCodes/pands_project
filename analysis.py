import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import the dataset via .csv file,
# & read through pandas
iris = pd.read_csv('iris.csv')

# Investigate shape of dataset
print(iris.shape)

# View sample of the dataset
print(iris.sample(10))

# View feature names
print(iris.columns[:-1])

# View target names
print(iris.species.unique())

# View data types
print(iris.dtypes)

# Generate descriptive statistics summary of dataset
print(iris.describe())

# Save summary as .txt file
with open('iris_summary.txt', 'w') as file:
    file.write(iris.describe().to_string())

# Check for missing values
print(iris.isnull().sum())

# Check for duplicates
print(iris.duplicated().sum())

# View duplicated rows
print(iris[iris.duplicated()])

# Check for balance in the target variable
sns.countplot(x ='species', hue = "species", data = iris)
plt.show()