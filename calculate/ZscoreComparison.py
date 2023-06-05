def compare_z_scores(x, mean_actor, std_dev_actor, mean_actress, std_dev_actress):
    z_actor = (x - mean_actor) / std_dev_actor
    z_actress = (x - mean_actress) / std_dev_actress
    return z_actor, z_actress

# Given values
age_winner_actor = 33
age_winner_actress = 45
mean_actor = 43.6
std_dev_actor = 5.6
mean_actress = 32.6
std_dev_actress = 12.3

# Calculate the z scores
z_actor, z_actress = compare_z_scores(age_winner_actor, mean_actor, std_dev_actor, mean_actress, std_dev_actress)

# Round the z scores to two decimal places
z_actor_rounded = round(z_actor, 2)
z_actress_rounded = round(z_actress, 2)

# Determine the winner with more extreme age
winner = "Best Actor" if abs(z_actor_rounded) > abs(z_actress_rounded) else "Best Actress"

# Print the results
print("The z score for the winner of Best Actor is z = {:.2f}".format(z_actor_rounded))
print("The z score for the winner of Best Actress is z = {:.2f}".format(z_actress_rounded))
print("Winner that had the more extreme age: {}".format(winner))
