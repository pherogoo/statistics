weight_5_27_lb = 5.27
mean_weight = 1.876
standard_deviation = 1.233

difference = weight_5_27_lb - mean_weight
rounded_difference = round(difference, 3)
print("a. The difference is", rounded_difference, "lb.")

standard_deviations = difference / standard_deviation
rounded_standard_deviations = round(standard_deviations, 2)
print("b. The difference is", rounded_standard_deviations, "standard deviations.")

z_score = standard_deviations
rounded_z_score = round(z_score, 2)
print("c. The z score is z =", rounded_z_score, ".")

if z_score >= -2 and z_score <= 2:
    significance = "not significant"
else:
    significance = "significantly high"
print("d. The highest weight is", significance + ".")
