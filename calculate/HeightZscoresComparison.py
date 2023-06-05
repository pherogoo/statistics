def calculate_z_score(x, mean, std_dev):
    return round((x - mean) / std_dev, 2)

# Given information
tallest_height = 218
shortest_height = 139.7
mean_height = 170.28
std_dev_height = 5.24

# Calculate z-scores
z_tallest = calculate_z_score(tallest_height, mean_height, std_dev_height)
z_shortest = calculate_z_score(shortest_height, mean_height, std_dev_height)

# Determine the man with the more extreme height
if abs(z_tallest) > abs(z_shortest):
    more_extreme_man = "tallest"
else:
    more_extreme_man = "shortest"

# Print the z-scores and the result
print("Z score for tallest man:", z_tallest)
print("Z score for shortest man:", z_shortest)
print("The", more_extreme_man, "man had the more extreme height.")
