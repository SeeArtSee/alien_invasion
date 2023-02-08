import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/death_valley_2018_full.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(header_row)
        print(index, column_header)

    dates, highs, lows = [], [], []
    # Первый способ как автоматизировать получение индексов
    # for ind_ex in header_row:
    #     if ind_ex == 'DATE':
    #         rd = header_row.index(ind_ex)
    #         print(rd)
    #     elif ind_ex == 'TMAX':
    #         rh = header_row.index(ind_ex)
    #         print(rh)
    #     elif ind_ex == 'TMIN':
    #         rl = header_row.index(ind_ex)
    #         print(rl)

    for r in reader:
        current_date = datetime.strptime(r[header_row.index('DATE')], '%Y-%m-%d')
        try:
            name = str(r[header_row.index('NAME')])
            high = int(r[header_row.index('TMAX')])
            low = int(r[header_row.index('TMIN')])
        except ValueError:
            print(f'Missing dada for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


print(highs)
print(lows)

# Нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# Форматирование диаграммы.
plt.title(name, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis="both", which='major', labelsize=16)
plt.show()


