import math

# Edit the values below
data = [10, 9, 2, 65, 81, 75, 86, 27, 26, 36, 95]

# Calculate range
data_range = max(data) - min(data)

# Calculate variance
mean = sum(data) / len(data)
squared_diffs = [(x - mean) ** 2 for x in data]
variance = sum(squared_diffs) / (len(data) - 1)  # Use (n-1) for sample variance

# Calculate standard deviation
standard_deviation = math.sqrt(variance)

# Print the results
print("Range:", data_range)
print("Variance:", variance)
print("Standard deviation:", standard_deviation)
