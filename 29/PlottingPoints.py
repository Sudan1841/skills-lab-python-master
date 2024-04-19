# MSU Denver - Skills Lab - 2020
# student: Abdulmajid Hasssan
# Description: Write a program that reads points from the user and then display them in a plot.

import matplotlib.pyplot as plt
X = []
Y = []
while True:
    line = input("? ")
    line = line.strip()
    if len(line) == 0:
        break
    x, y = line.split(",")
    x = float(x)
    y = float(y)
    X.append(x)
    Y.append(y)
plt.scatter(X, Y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

