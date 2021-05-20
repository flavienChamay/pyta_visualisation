"""
Manage random walks.

This is random decisions about which direction the walk should take.

:class: RandomWalk()
"""

from random import choice


class RandomWalk:
    """
    Generate random walks.

    :method: __init__(self, num_points=5000)
    :method: fill_walk(self)
    """

    def __init__(self, num_points=5000):
        """
        Initialize and generate attributes and RandomWalk instance.

        :param var num_points int: Number of points to generate.
        :var x_values list: The walk start at x = 0.
        :var y_values list: The walk start at y = 0.
        :returns: RandomWalk.
        """
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """
        Calculate all the points in the walk.

        If the value of both x_step and y_step are 0 the walk doesn't go anywhere.

        :var x_direction int: 1 for a right movement, -1 for a left movement
        :var x_distance int: Integer between 0 and 4 telling how far to move into the x_direction direction.
        :var x_step int: Length of each step in the x direction. 
        A positive result means move right, a negative result means move left.
        0 means move horizontally
        :var y_direction int: Idem as x_direction.
        :var y_distance int: Idem as x_distance.
        :var y_step int: Idem as x_step.
        :returns: None.
        """
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
