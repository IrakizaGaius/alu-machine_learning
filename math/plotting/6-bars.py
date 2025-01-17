import numpy as np
import matplotlib.pyplot as plt


np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

labels = ['Farrah', 'Fred', 'Felicia']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
fruit_labels = ['apples', 'bananas', 'oranges', 'peaches']
fig, ax = plt.subplots()
bar_width = 0.5

bottoms = np.zeros(fruit.shape[1])
for i in range(fruit.shape[0]):
    ax.bar(labels, fruit[i], bottom=bottoms, color=colors[i], width=bar_width, label=fruit_labels[i])
    bottoms += fruit[i]


ax.set_ylabel('Quantity of Fruit')
ax.set_yticks(np.arange(0, 81, 10))
ax.set_ylim(0, 80)
ax.set_title('Number of Fruit per Person')
ax.legend()
plt.show()
