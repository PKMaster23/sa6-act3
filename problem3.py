def find_maximum(numbers, which_is_greater):
    maximum = numbers[0]

    for num in numbers[1:]:
        maximum = which_is_greater(maximum, num)

    return maximum

numbers_list = [23, 13, 11, 25, 8, 2]
which_is_greater = lambda x, y: x if x > y else y

result = find_maximum(numbers_list, which_is_greater)
print(f'The maximum nunmber is: {result}')