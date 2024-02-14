sum_of_digits = lambda num: sum(int(digit) for digit in str(num) if digit.isdigit())

num = 123

print(sum_of_digits(num))