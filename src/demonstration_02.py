"""
Challenge #2:

Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.

Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes:
- The input list will only contain integers.
"""

# U.P.E.R:
    # UNDERSTAND
        # given a string
        #  numbers with ", " seperators
        #  need to multiply all numbers in strings
    # EDGE CASES
        # can it have negatives or decimals? No
        # one number? sure
        # empty string? no
    # PLAN
        # break into sub problems:
            # convert input into numbers
                # convert with use.split(", ") with comma and space as key, it will give us an array of numbers
                    # test around with print(nums.split(', '))
            # maybe an array
            # Multiple array of numbers
                #  final_val = 1
                #  for loop over all nums
                    # turn into int
                    # multiply into final_val

def add_indexes(numbers):
    nums_array = nums.split(', ')
    final_val = 1
    for num in nums_array:
        final_val *= int(num)
    return final_val

print(add_indexes([0, 0, 0, 0, 0])) # ➞ [0, 1, 2, 3, 4]
print(add_indexes([1, 2, 3, 4, 5])) # ➞ [1, 3, 5, 7, 9]
print(add_indexes([5, 4, 3, 2, 1])) # ➞ [5, 5, 5, 5, 5]