"""
Manage the visualization of square number sequence.

:var squares list: List of square numbers.
:var fig Figure: Represent the entire figure or collection of plots that are generated.
:var ax axes.Axes: Represent a single plot in the figure.
"""

import matplotlib.pyplot as plt
from matplotlib import use
use('tkagg')
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)

plt.show()
