# Remove even numbers
def filter_even_numbers(listy):
    new_list = []
    for i in listy:
        if i % 2 != 0:
            new_list.append(i)
    return new_list

# Remove Odd numbers
def filter_odd_numbers(listy):
    new_list = []
    for i in listy:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print(filter_even_numbers([1,2,3,4,5,6,7,8,9,10]))
print(filter_odd_numbers([1,2,3,4,5,6,7,8,9,10]))

# Duplicate Filters
def remove_duplicates(nums):
    my_set = set()
    for i in nums:
        if i not in my_set:
            my_set.add(i)
    return list(my_set)

print(remove_duplicates([5,5,5,5,6,6,7,8,9]))