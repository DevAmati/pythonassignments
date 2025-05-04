# Data Analysis and Visualization Assignment
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set the style for our plots
plt.style.use('seaborn-v0_8')

# Task 1: Load and Explore the Dataset
print("Task 1: Loading and Exploring the Dataset")
print("-" * 50)

# Load the Iris dataset
try:
    # Load from sklearn datasets
    iris = load_iris()
    
    # Create a pandas DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    
    # Add the target column (species)
    df['species'] = [iris.target_names[i] for i in iris.target]
    
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# Display the first few rows of the dataset
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Explore the structure of the dataset
print("\nDataset information:")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print("\nData types:")
print(df.dtypes)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# If there were missing values, we would clean them here
# Since Iris dataset doesn't have missing values, we'll add a comment
print("\nThe dataset has no missing values, so cleaning is not necessary.")

# Task 2: Basic Data Analysis
print("\nTask 2: Basic Data Analysis")
print("-" * 50)

# Compute basic statistics
print("\nBasic statistics for numerical columns:")
print(df.describe())

# Perform groupings on a categorical column
print("\nMean values grouped by species:")
species_means = df.groupby('species').mean()
print(species_means)

# Identify patterns
print("\nInteresting findings:")
print("1. Setosa species has the smallest petal length and width.")
print("2. Virginica species has the largest petal and sepal dimensions on average.")
print("3. There's a clear separation between species based on petal size.")

# Task 3: Data Visualization
print("\nTask 3: Data Visualization")
print("-" * 50)
print("Creating visualizations... (Check the output figures)")

# Create a figure with subplots
plt.figure(figsize=(20, 15))

# 1. Line chart showing trends
# For demonstration, we'll create a line chart of sorted sepal length for each species
plt.subplot(2, 2, 1)
for species in iris.target_names:
    temp_df = df[df['species'] == species].copy()
    temp_df = temp_df.sort_values('sepal length (cm)')
    plt.plot(range(len(temp_df)), temp_df['sepal length (cm)'], label=species)
plt.title('Sorted Sepal Length by Species', fontsize=14)
plt.xlabel('Index', fontsize=12)
plt.ylabel('Sepal Length (cm)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

# 2. Bar chart for comparison across categories
plt.subplot(2, 2, 2)
species_means.plot(kind='bar', ax=plt.gca())
plt.title('Average Measurements by Species', fontsize=14)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Measurement (cm)', fontsize=12)
plt.grid(True, alpha=0.3)

# 3. Histogram to understand distribution
plt.subplot(2, 2, 3)
plt.hist(df['petal length (cm)'], bins=20, alpha=0.7, color='blue', edgecolor='black')
plt.title('Distribution of Petal Length', fontsize=14)
plt.xlabel('Petal Length (cm)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, alpha=0.3)

# 4. Scatter plot for relationship between two columns
plt.subplot(2, 2, 4)
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
for species in iris.target_names:
    temp_df = df[df['species'] == species]
    plt.scatter(
        temp_df['sepal length (cm)'], 
        temp_df['petal length (cm)'],
        c=colors[species],
        label=species,
        alpha=0.7
    )
plt.title('Sepal Length vs Petal Length', fontsize=14)
plt.xlabel('Sepal Length (cm)', fontsize=12)
plt.ylabel('Petal Length (cm)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

# Adjust layout and display
plt.tight_layout()
plt.savefig('iris_visualizations.png')
plt.show()

print("\nAnalysis complete! All tasks have been performed successfully.")
print("The visualizations have been generated and displayed.")

# Additional visualization: Pair plot for more comprehensive view
print("\nGenerating pair plot for all features...")
sns.pairplot(df, hue='species')
plt.suptitle('Pair Plot of Iris Dataset', y=1.02, fontsize=16)
plt.savefig('iris_pairplot.png')
plt.show()

print("\nSummary of findings:")
print("1. The three Iris species (setosa, versicolor, and virginica) show distinct patterns in their measurements.")
print("2. Setosa is clearly separable from the other two species based on petal dimensions.")
print("3. Versicolor and virginica have some overlap but can generally be distinguished.")
print("4. Petal length and width show stronger correlation with species than sepal measurements.")
print("5. There is a positive correlation between petal length and petal width across all species.")