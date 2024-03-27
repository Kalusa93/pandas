import matplotlib.pyplot as plt
import pickle

with open('avoplotto.pkl', 'rb') as f:
    avocados = pickle.load(f)

# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()

# We can see that on average, organic avocados are more expensive than conventional ones, 
# but their price distributions have some overlap.