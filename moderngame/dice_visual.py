import plotly
from plotly.graph_objects import Bar, Layout
from plotly import offline
from die import Die

"""Создание кубика D6"""
die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
[results.append(die_1.roll() + die_2.roll() + die_3.roll()) for roll_num in range(100000)]

"""Анализ результатов"""
frequencies = []
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
[frequencies.append(results.count(value)) for value in range(3, max_results+1)]

"""Визуализация результатов"""
x_values = list(range(3, max_results+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 and D8 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')

