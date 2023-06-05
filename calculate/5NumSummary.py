import numpy as np

# Given data
ratings = [3.0, 3.0, 4.0, 4.5, 4.5, 4.5, 5.5, 5.5, 5.5, 5.5, 5.5, 6.5, 6.5, 7.0, 7.0, 7.0, 7.5, 7.5, 7.5, 7.5]

# Calculate the 5-number summary
min_val = np.min(ratings)
q1 = np.percentile(ratings, 25)
median = np.percentile(ratings, 50)
q3 = np.percentile(ratings, 75)
max_val = np.max(ratings)

# Print the 5-number summary
print("The 5-number summary is:")
print("1:", min_val)
print("2:", q1)
print("3:", median)
print("4:", q3)
print("5:", max_val)
