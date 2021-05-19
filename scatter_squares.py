"""
Manages the plotting of single points.

:var x_values list: List of x values.
:var y_values list: List of y values.
:var fig Figure: Represent the entire figure or collection of plots that are generated.
:var ax axes.Axes: Represent a single plot in the figure.
"""

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# Color can be c='name_of_color' or c=(float R, float G, float B) with R, G and B between 0 and 1
#ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=5)
# Color using colormap.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1_100, 0, 1_100_000])

plt.show()
# If you want to save the plot in a file then replace plt.show with:
#plt.savefig('squares_plot.png', bbox_inches='tight')
