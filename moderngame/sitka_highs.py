import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows, prcp = [], [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        prc = float(row[3])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        prcp.append(prc)


print(header_row)
print(highs)
print(lows)
print(prcp)

# Нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates, prcp, c='green')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# Форматирование диаграммы.
plt.title("Daily high temperatures, 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Величина осадков %', fontsize=16)
plt.tick_params(axis="both", which='major', labelsize=16)
plt.show()

