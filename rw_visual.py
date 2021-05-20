"""
Plot all the points in the walk.

:var rw RandomWalk: The random walk generated.
:var fig Figure: Represent the entire figure or collection of plots that are generated.
:var ax axes.Axes: Represent a single plot in the figure.
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
