#In this exercise, you'll visualize the change in avocado sales over three years.

import matplotlib.pyplot as plt
import pickle

with open('avoplotto.pkl', 'rb') as f:
    avocados = pickle.load(f)

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind='line')

# Show the plot
plt.show()

# Here, it looks like the number of avocados spikes around the same time each year.