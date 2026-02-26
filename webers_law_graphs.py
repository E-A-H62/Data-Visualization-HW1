from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


"""Elena's graphs"""
# regular bar graph (no gridlines)
y = [50, 99, 84, 112, 127, 130, 102]
x = ["Tomatoes", "Onions", "Potatoes", "Carrots", "Lettuce", "Broccoli", "Cucumbers"]
plt.title("Vegetables Purchased")
plt.xlabel("Vegetables")
plt.xticks(rotation=45)
plt.ylabel("Number of Purchases")
plt.bar(x, y)
plt.show()
# bar graph with gridlines (only x axis gridlines)
x2 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
y2 = y[::-1]
y2 = [int(x) * 2 for x in y2]
plt.title("Number of Customers in a Week")
plt.xlabel("Days of the Week")
plt.xticks(rotation=45)
plt.ylabel("Number of Customers")
plt.bar(x2, y2)
plt.grid(True)
plt.grid(axis='x')
plt.show()
# bar graph with dot grid
plt.title("Temperatures in a Week")
plt.xlabel("Days of the Week")
plt.xticks(rotation=45)
plt.ylabel("Temperature (F)")
plt.bar(x2, y)
plt.grid(True, linestyle=':')
plt.show()

"""Paul's graphs"""
# Load the Iris dataset from GitHub
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

colors = {'setosa': 'crimson', 'versicolor': 'steelblue', 'virginica': 'green'}

# Scatterplot (no guidelines)
plt.scatter(df['sepal_length'], df['petal_length'], color='steelblue', edgecolors='black', alpha=0.6)
plt.title("Iris: Sepal Length vs Petal Length (No Aids)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# Scatterplot (Colored by species + trend line)
for species, group in df.groupby('species'):
    plt.scatter(group['sepal_length'], group['petal_length'],
                label=species, color=colors[species], edgecolors='black', alpha=0.7)

# Best-fit line
def best_fit(x, y):
    m = (x * y - x.mean() * y.mean()).sum() / ((x ** 2) - x.mean() ** 2).sum()
    b = y.mean() - m * x.mean()
    return m, b

m, b = best_fit(df['sepal_length'], df['petal_length'])
x_line = pd.Series([df['sepal_length'].min(), df['sepal_length'].max()])
plt.plot(x_line, m * x_line + b, color='black', linewidth=2, linestyle='--', label='Best-Fit Line')

plt.title("Iris: Sepal Length vs Petal Length (By Species)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# Scatterplot (Data Aggregation)
agg = df.groupby('species')[['sepal_length', 'petal_length']].mean()

for species, group in df.groupby('species'):
    plt.scatter(group['sepal_length'], group['petal_length'],
                color=colors[species], edgecolors='black', alpha=0.2)

for species, row in agg.iterrows():
    plt.scatter(row['sepal_length'], row['petal_length'],
                color=colors[species], edgecolors='black', s=200, zorder=5,
                label=f'{species} (mean)')

plt.title("Iris: Sepal Length vs Petal Length (Data Aggregation)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

"""Megan's Graphs"""
# Creating the dataset
X, y = make_blobs(n_samples=500, centers=3, n_features=2, random_state=236)
X = X + 22  # Shift the data to make it more visually appealing

# Scatterplot (no guidelines)
plt.scatter(X[:, 0], X[:, 1], c="teal", alpha=0.75)
plt.xlabel('Age (Years)')
plt.ylabel('Number of Friends')
plt.title('Age vs. Number of Friends by Level of School')
plt.show()

# Scatterplot (Colored by cluster + trend line)
# Calculate the best-fit line
m, b = np.polyfit(X[:, 0], X[:, 1], 1)

# Create line values
x_line = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
y_line = m * x_line + b

# Plot line
plt.plot(x_line, y_line, c="black", linestyle="dashed")

# Plot the data
array = np.array([0,1,2])
scatter = plt.scatter(X[:, 0], X[:, 1], c=y, cmap="summer", alpha=0.75)

handles, labels = scatter.legend_elements()
labels = ["Elementary", "High School", "College"]

plt.xlabel('Age (Years)')
plt.ylabel('Number of Friends')
plt.title('Age vs. Number of Friends by Levels of School')
plt.legend(handles, labels, title="Clusters")
plt.show()


# Scatterplot (Data Aggregation)
# Calculate centroids for each cluster
centroids = np.array([
    X[y == cluster].mean(axis=0)
    for cluster in np.unique(y)
])

# Plot the data
array = np.array([0,1,2])
scatter = plt.scatter(X[:, 0], X[:, 1], c=y, cmap="summer", alpha=0.5)

handles, labels = scatter.legend_elements()
labels = ["Elementary (mean)", "High School (mean)", "College (mean)"]
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    c=array,
    cmap="summer",
    edgecolors="black",
    s=200  # size of marker
)
plt.xlabel('Age (Years)')
plt.ylabel('Number of Friends')
plt.title('Age vs. Number of Friends by Levels of School')
plt.legend(handles, labels, title="Clusters")
plt.show()