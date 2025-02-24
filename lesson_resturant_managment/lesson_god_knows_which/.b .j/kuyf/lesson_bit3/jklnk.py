def divide_without_divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    
    quotient = 0
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    
    return sign * quotient

result = divide_without_divide(10, 2)
print("10 divided by 2 is:", result) 