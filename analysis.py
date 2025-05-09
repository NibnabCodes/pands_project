import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn as skl
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict


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

# Load from sklearn
iris = load_iris()
# Convert to DataFrame & extract features
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Compute correlation matrix
corr_matrix = df.corr()

# Display
print(corr_matrix)

# Create figure, axis & subplots
fig, ax = plt.subplots(figsize=(8, 6))

# Plot & Display heatmap with customised colours
cax = ax.imshow(corr_matrix, cmap='PiYG')

# Add color bar
fig.colorbar(cax)

# Set feature names as labels
ax.set_xticks(range(len(df.columns)), labels=df.columns,
              rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticks(range(len(df.columns)), labels=df.columns)

# Add grid lines
plt.grid()

# Display title
plt.title("Correlation Heatmap of Iris Features", fontsize=16)
plt.show()

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Add subplot title
fig.suptitle("Iris Feature Distribution by Species", fontsize=16)

# Create violin plots for each feature & add titles
sns.violinplot(x='species', y='sepal_length', data=iris_df, ax=axes[0, 0], hue='species', palette="husl")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_title("Sepal Length by Species")

sns.violinplot(x='species', y='sepal_width', data=iris_df, ax=axes[0, 1], hue='species', palette="husl")
axes[0, 1].set_ylabel("Frequency")
axes[0, 1].set_title("Sepal Width by Species")

sns.violinplot(x='species', y='petal_length', data=iris_df, ax=axes[1, 0], hue='species', palette="husl")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].set_title("Petal Length by Species")

sns.violinplot(x='species', y='petal_width', data=iris_df, ax=axes[1, 1], hue='species', palette="husl")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].set_title("Petal Width by Species")

# Adjust layout
plt.tight_layout()
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

# Load features and target from sklearn
X = iris.data  # Features (sepal & petal measurements)
y = iris.target  # class labels (species)

# Split the dataset - training & test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Logistic Regression model
# & store it in variable
model = LogisticRegression(solver='lbfgs', max_iter=200)
# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on unseen data (test set)
# & store in variable
y_pred = model.predict(X_test)

# Generate accuracy score of the model
accuracy = accuracy_score(y_test, y_pred)

# Print accuracy score
print(f"Accuracy: {accuracy:.2f}")

# Generate & print classification report
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Generate & print confusion matrix
print(confusion_matrix(y_test, y_pred))

# Evaluate & predict model with 5-fold cross-validation
cv_scores = cross_val_score(model, X, y, cv=5)
print("Cross-validation scores:", cv_scores)
print("Mean cross-validation score:", cv_scores.mean().round(2))

# Predict labels using 5-fold cross-validation
predicted_labels = cross_val_predict(model, X, y, cv=5)

# Print the cross-val confusion matrix
print(confusion_matrix(y, predicted_labels))