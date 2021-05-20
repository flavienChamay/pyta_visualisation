"""
Main program of the die visualization.

Prints the results of a die.

:var die_1 Die: First die to visualize.
:var die_1 Die: Second die to visualize.
:var results list: The results of the die.
:var result int: The result of the die in one iteration.
"""
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create two D6 and D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(50_000)]

# Analyse the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 50 000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

# Generate the plot in a html file.
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')

print(frequencies)
