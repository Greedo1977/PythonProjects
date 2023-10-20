from matplotlib import pyplot as plt
from pathlib import Path

input_values = range(1,1001)
squares = [value**2 for value in input_values]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.set_title("Square Numbers", fontsize = 20)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

ax.tick_params(labelsize = 14)

ax.scatter(input_values, squares, c = squares, cmap = plt.cm.OrRd, s=10)

ax.ticklabel_format(style='plain')
#plt.show()
file = Path('../Resources/squares_plot.png')

plt.savefig(file, bbox_inches = 'tight')