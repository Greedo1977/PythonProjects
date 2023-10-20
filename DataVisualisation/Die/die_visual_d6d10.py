import plotly.express as px
from die import Die
from DieFunctions import input_range, number_sides

range_ = input('Enter max range: ')
max_range = input_range(range_)



sides1 = input('Enter sides of Die 1: ')
sides2 = input('Enter sides of Die 2: ')

die1 = Die(number_sides(sides1))
die2 = Die(number_sides(sides2))

results = []

for _ in range(1, max_range):
    max_value = max([die1.roll(), die2.roll()])
    results.append(max_value)

sum_of_results = sum(results)

frequencies = []

poss_results = range(1, (max(list([die1.num_sides, die2.num_sides])))+1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

average_result = sum_of_results/max_range

print(f"Average result of rolling 2 and taking the highest is about {average_result/100:.3%}")

#Visualise the results.
title = f'Results of Rolling two D{die1.num_sides} {max_range} times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
fig.update_layout(title_x = 0.5)
fig.update_layout(xaxis_dtick=1)

fig.show()