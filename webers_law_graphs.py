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