import matplotlib.pyplot as plt

squares = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_styles = ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery',
                  '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background',
                  'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn',
                  'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark',
                  'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep',
                  'seaborn-muted', 'seaborn-notebook', 'seaborn-paper',
                  'seaborn-pastel', 'seaborn-poster', 'seaborn-talk',
                  'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
x_values = [2.5, 3.5, 4.5, 5.5, 6, 7, 8, 8, 7,6]
y_values = [100, 150, 200, 250, 350, 450,600, 750,800,800]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.set_title('Кубы чисел', fontsize=24)
ax.set_xlabel('Значения', fontsize=14)
ax.set_ylabel('Кубы значений', fontsize=14)
ax.tick_params(axis='both',which ='major', labelsize=14)
ax.scatter(x_values, y_values, s=200)
plt.show()