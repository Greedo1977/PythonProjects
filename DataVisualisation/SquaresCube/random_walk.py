from random import choice


def get_direction():
    x_direction = choice([1, -1])
    y_direction = choice([1, -1])
    return x_direction, y_direction


def get_distance():
    x_distance = choice(range(0, 9))
    y_distance = choice(range(0, 9))

    return x_distance, y_distance


def get_step():
    direction = get_direction()
    distance = get_distance()

    x_direction = direction[0]
    x_distance = distance[0]
    x_step = x_direction * x_distance

    y_direction = direction[1]
    y_distance = distance[1]
    y_step = y_distance * y_direction

    return x_step, y_step


class RandomWalk:

    def __init__(self, num_points = 5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.num_points:

            step = get_step()
            x_step = step[0]
            y_step = step[1]

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
