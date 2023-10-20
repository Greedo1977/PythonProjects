import plotly.express as px
from die import Die
from DieFunctions import input_range, number_sides

range_ = input('Enter max range: ')
sides = input('Enter sides of Die ')

max_range = input_range(range_)

die1 = Die(number_sides(sides))
die2 = Die(number_sides(sides))

results = []

for roll_num in range(1, max_range):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []

poss_results = range(2, die1.num_sides*2 + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#Visualise the results.
title = f'Results of Rolling two D{die1.num_sides} {max_range} times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
fig.update_layout(title_x = 0.5)
fig.update_layout(xaxis_dtick=3)

fig.show()