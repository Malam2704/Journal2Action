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

# Bonus, Palindrme Checker
def is_palindrome(my_str):
    my_len = len(my_str)
    for i in range(0, my_len):
        if(my_str[i] != my_str[my_len - (i+1)]):
            return False
    return True

print(is_palindrome("tacocat"))
print(is_palindrome("tacocato"))

def vowel_counter(my_string):
    vowels = ['a','e','i','o','u']
    vowel_dict = {}
    for letter in my_string:
        if letter in vowels:
            if letter in vowel_dict:
                vowel_dict[letter] += 1
            else:
                vowel_dict[letter] = 1
    return vowel_dict

print(vowel_counter("my vowel counter"))