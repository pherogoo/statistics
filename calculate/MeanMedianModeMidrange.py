from statistics import mean, median
from collections import Counter

data = [74, 71, 37, 52, 93, 46, 83, 69, 48, 77, 33]

print()

print("Data:", data)

mean_value = round(mean(data), 1)
print("Mean:", mean_value)

median_value = median(data)
print("Median:", median_value)

counter = Counter(data)
frequencies = counter.values()
max_frequency = max(frequencies)

mode = [k for k, v in counter.items() if v == max_frequency]

if len(mode) == len(data) or len(mode) == 0:
    print("No mode")
else:
    print("Mode:", *mode)

print("Counter:", counter)
print("Frequencies:", frequencies)
print("Max Frequency:", max_frequency)

# Midrange calculation
min_value = min(data)
max_value = max(data)
midrange_formula = "(Minimum value + Maximum value) / 2"
midrange_variables = {"Minimum value": min_value, "Maximum value": max_value}
midrange_value = (midrange_variables["Minimum value"] + midrange_variables["Maximum value"]) / 2
print("Midrange:", midrange_value)
print("Midrange Calculation: Midrange =", midrange_formula.replace("Minimum value", str(midrange_variables["Minimum value"])).replace("Maximum value", str(midrange_variables["Maximum value"])))
print("Variable Values:", midrange_variables)
