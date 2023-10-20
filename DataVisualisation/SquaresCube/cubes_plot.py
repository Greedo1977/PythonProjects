from matplotlib import pyplot as plt
from pathlib import Path
file = Path('../Resources/cubes.png')

values = range(1,11)
cubes = [value**3 for value in values]
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(values, cubes, color = 'red', linewidth=3)

ax.set_ylabel('Cubes', fontsize = 14)
ax.set_xlabel('Value', fontsize = 14)
ax.set_title("Showing cubes", fontsize=20)
ax.tick_params(labelsize=10)

ax.scatter(values, cubes, c = cubes, cmap = plt.cm.OrRd)

savefile = input("Do you wish to save plot? (y/n) ")

if savefile.upper() == 'Y':
    plt.savefig(file)

plt.show()