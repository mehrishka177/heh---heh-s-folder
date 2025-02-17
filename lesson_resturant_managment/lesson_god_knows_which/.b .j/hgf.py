from collections import Counter

# Sample list of numbers
numbers = [1, 2, 3, 1, 2, 1, 4, 5, 6, 5, 2, 3, 4, 4, 4]

# Count the occurrences of each number
number_counts = Counter(numbers)

# Print the occurrences
print("Number occurrences:")
for number, count in number_counts.items():
    print(f"Number {number}: {count} time(s)")



