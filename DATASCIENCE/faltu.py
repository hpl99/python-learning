import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [10, 20, 30]
plt.plot(x, y)
plt.xticks(rotation=45)
plt.yticks(rotation=-45)
plt.show()