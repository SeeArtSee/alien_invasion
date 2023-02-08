import matplotlib .pyplot as plt

x_values = list(range(1000))
y_values = [x**3 for x in x_values]


plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.set_title('Точечная диаграмма', fontsize=25)
ax.set_xlabel('Значения', fontsize=14)
ax.set_ylabel('Квадраты значений', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.axis([0, 1000, 0, 1100000000])
plt.show()