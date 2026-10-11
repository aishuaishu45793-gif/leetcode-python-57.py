# 129. Find the Second-Largest Number

numbers = [10, 25, 8, 40, 30, 40]

unique_numbers = sorted(set(numbers), reverse=True)

if len(unique_numbers) >= 2:
    print("Second-largest number:", unique_numbers[1])
else:
    print("A second-largest distinct number does not exist")