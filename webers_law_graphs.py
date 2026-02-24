import matplotlib.pyplot as plt
import pandas as pd


"""Elena's graphs"""
# regular bar graph (no gridlines)
y = [50, 99, 84, 102, 127, 130, 112]
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
