n = int(input("Enter the number of rows: "))

# Displaying the mirrored right-angled triangle
print("\nMirrored Triangle:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

print("\nMirrored Triangle Pattern Completed!")
print("Thank you for using the program.")

# Additional Feature: Display triangle in reverse
print("\nReversed Mirrored Triangle:")
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)

# Displaying a full pyramid pattern
print("\nFull Pyramid Pattern:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Displaying an inverted full pyramid pattern
print("\nInverted Full Pyramid Pattern:")
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print("\nAll patterns displayed successfully.")
print("\nProgram Execution Finished.")