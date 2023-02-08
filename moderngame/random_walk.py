from random import choice
import matplotlib.pyplot as plt


class RandomWalk:
    """Класс для генерирования случайных блужданий"""

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        for i in range(len(self.x_values), self.num_points):
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.y_values.append(y)
            self.x_values.append(x)

    def fill_walk(self):
        self.get_step()


rw = RandomWalk()
rw.fill_walk()

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(12, 7))

point_numbers = range(rw.num_points)

ax.plot(rw.x_values, rw.y_values, c='Blue', linewidth=1)

ax.scatter(rw.x_values, rw.y_values, c='Red', edgecolors=None, s=10)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()




