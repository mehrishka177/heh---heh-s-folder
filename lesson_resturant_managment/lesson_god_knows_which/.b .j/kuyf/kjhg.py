import math

# Prompt the user to input a base and an exponent
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))

# Calculate the power using logarithms
result = math.exp(exponent * math.log(base))

# Print the result
print(f"The result of {base} to the power of {exponent} is {result}")