#In this exercise, you'll compare the number of avocados sold to average price and see if they're at all related. 
#If they're related, you may be able to use one number to predict the other.

import matplotlib.pyplot as plt
import pickle

with open('avoplotto.pkl', 'rb') as f:
    avocados = pickle.load(f)

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(kind='scatter', x='nb_sold', y='avg_price', title='Number of avocados sold vs. average price')

# Show the plot
plt.show()

# It looks like when more avocados are sold, prices go down.'
# However, this doesnt mean that fewer sales causes higher prices:'
# we can only tell that they are correlated with each other.