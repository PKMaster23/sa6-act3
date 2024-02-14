def find_intersection(list1, list2):
    intersection = list(filter(lambda x: x in list2, list1))
    return intersection

list1 = [2, 4, 6, 8]
list2 = [5, 6, 7, 8]

result = find_intersection(list1, list2)
print(f'The intersection of the two lists yields: {result}')