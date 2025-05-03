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

# Check for missing values
print(iris.isnull().sum())

# Check for duplicates
print(iris.duplicated().sum())

# View duplicated rows
print(iris[iris.duplicated()])

# Drop duplicates
iris_df = iris.drop_duplicates()

# Check for balance in the target variable
sns.countplot(x ='species', hue = "species", data = iris_df)
plt.show()

# Generate descriptive statistics summary of dataset
print(iris_df.describe())

# Save summary as .txt file
with open('iris_summary.txt', 'w') as file:
    file.write(iris_df.describe().to_string())

# Create subplots
fig, ax = plt.subplots(2, 2, figsize=(8, 6))

# Create histogram for sepal length
ax[0,0].hist(iris_df['sepal_length'], bins=6, color='green', edgecolor='black')
# Set the figure title
ax[0,0].set_title("Sepal Length")

# Create histogram for sepal width
ax[0,1].hist(iris_df['sepal_width'], bins=5, color='red', edgecolor='black')
# Set the figure title
ax[0,1].set_title("Sepal Width")

# Create histogram for petal length
ax[1,0].hist(iris_df['petal_length'], bins=6, color='blue', edgecolor='black')
# Set the figure title
ax[1,0].set_title("Petal Length")

# Create histogram for petal width
ax[1,1].hist(iris_df['petal_width'], bins=6, color='purple', edgecolor='black')
# Set the figure title
ax[1,1].set_title("Petal Width")

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()

# Create boxplot of each feature
sns.boxplot(data=iris_df, orient='v', palette='Set3')
plt.show()

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Add subplot title
fig.suptitle("Iris Feature Distribution by Species", fontsize=16)

# Create violin plots for each feature & add titles
sns.violinplot(x='species', y='sepal_length', data=iris, ax=axes[0, 0], hue='species', palette="husl")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_title("Sepal Length by Species")

sns.violinplot(x='species', y='sepal_width', data=iris, ax=axes[0, 1], hue='species', palette="husl")
axes[0, 1].set_ylabel("Frequency")
axes[0, 1].set_title("Sepal Width by Species")

sns.violinplot(x='species', y='petal_length', data=iris, ax=axes[1, 0], hue='species', palette="husl")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].set_title("Petal Length by Species")

sns.violinplot(x='species', y='petal_width', data=iris, ax=axes[1, 1], hue='species', palette="husl")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].set_title("Petal Width by Species")

# Adjust layout
plt.tight_layout()
plt.savefig('iris_violinplots.png')
plt.show()

# load iris dataset
# from seaborn online library
df = sns.load_dataset('iris')

# Create pairplot of the dataset
df = sns.pairplot(df, hue='species', palette='husl')

# Adjust position of title higher
# to prevent it from obstructing
# the plots
df.figure.subplots_adjust(top=.9)

# Add title
df.figure.suptitle("Pairplot of Iris Dataset", fontsize=16)
plt.show()
