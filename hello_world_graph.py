import matplotlib.pyplot as plt
import pandas as pd


X = ["Apples", "Bananas", "Cherries"]
Y = [25, 43, 89]

plt.title("Number of Fruits")
plt.xlabel("Fruit")
plt.ylabel("Number of Fruits")
plt.bar(X, Y)
plt.show()


# more complicated graph
data = pd.read_csv('heart.csv')

print(data.head())

