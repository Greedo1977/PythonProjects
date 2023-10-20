from matplotlib import pyplot as plt


input_values = range(1,11)
squares = [value**2 for value in input_values]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)
ax.set_title("Square Numbers", fontsize = 20)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

ax.tick_params(labelsize = 14)

ax.scatter(2,4, color='red', s=200)

plt.show()