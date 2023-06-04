import numpy as np

# Here's the question that needs to be answered:

"""
The blood platelet counts of a group of women have a bell-shaped distribution with a mean of 'mean'
and a standard deviation of 'std_dev'.
(All units are 1000 cells/muL.)

Using the empirical rule, find each approximate percentage below.

a. What is the approximate percentage of women with platelet counts within 1
   standard deviation of the mean, or between 'range_a[0]' and 'range_a[1]'?

b. What is the approximate percentage of women with platelet counts between 'range_b[0]' and 'range_b[1]'?
"""

# Edit the values below
mean = 247.1
std_dev = 67.5
range_a = (179.6, 314.6)
range_b = (44.6, 449.6)

def calculate_percentage_within_range(data, range_values):
    within_range = len([x for x in data if range_values[0] <= x <= range_values[1]]) / len(data)
    return within_range

# Generate a sample of platelet counts
np.random.seed(42)  # For reproducibility
sample_size = 10000
platelet_counts = np.random.normal(mean, std_dev, sample_size)

# Calculate the approximate percentage within the ranges
percentage_within_range_a = calculate_percentage_within_range(platelet_counts, range_a)
percentage_within_range_b = calculate_percentage_within_range(platelet_counts, range_b)

# Print the results
print("Approximate percentage within range a: {:.2%}".format(percentage_within_range_a))
print("Approximate percentage within range b: {:.2%}".format(percentage_within_range_b))
