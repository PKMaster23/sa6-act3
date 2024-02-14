list_of_fruits = ['dragonfruit', 'banana', 'rasberry', 'apple', 'cherry',]

sorted_list = sorted(list_of_fruits, key=lambda s: (len(s), s))

print(sorted_list)