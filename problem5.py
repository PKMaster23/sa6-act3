def power_of_n(numbers, n):
    powered_numbers = list(map(lambda x: x ** n, numbers))
    return powered_numbers

numbers = [5, 6, 7, 8]
n = 2

result = power_of_n(numbers, n)
print(f"Numbers raised to the power of {n}: {result}")