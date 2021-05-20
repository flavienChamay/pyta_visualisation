"""
Manage the behavior of a die.

:class: Die()
"""

from random import randint


class Die:
    """
    Manage and generate the behavior of a die.

    :method: __init__(self, num_sides=6)
    :method: roll(self)
    """

    def __init__(self, num_sides=6):
        """
        Initialize a six-sided die.

        :param num_sides int: The number of sides of the die. By default equal to 6.
        :returns: Die.
        """
        self.num_sides = num_sides

    def roll(self):
        """
        Return a random value between 1 and number of sides.

        :returns: int.
        """
        return randint(1, self.num_sides)
