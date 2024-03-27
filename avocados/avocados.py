#Which avocado size is most popular?
#Avocados are increasingly popular and delicious in guacamole and on toast. 
#The Hass Avocado Board keeps track of avocado supply and demand across the USA, 
#including the sales of three different sizes of avocado. In this exercise, you'll use a bar plot 
#to figure out which size is the most popular.

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
import pickle

with open('avoplotto.pkl', 'rb') as f:
    avocados = pickle.load(f)

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind='bar', color='skyblue')

# Set the labels of the x-axis ticks horizontally
plt.xticks(rotation=0)

# Show the plot

plt.show()

# It looks like small avocados were the most-purchased size, but large avocados were a close second.