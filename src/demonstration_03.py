"""
Challenge #3:

Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20

Notes:
- Bonus: Try to complete this challenge in one line!
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

def multiply_nums(nums):
     nums_array = nums.split(', ')
    final_val = 1
    for num in nums_array:
        final_val *= int(num)
    return final_val

print(add_indexes([0, 0, 0, 0, 0])) # ➞ [0, 1, 2, 3, 4]
print(add_indexes([1, 2, 3, 4, 5])) # ➞ [1, 3, 5, 7, 9]
print(add_indexes([5, 4, 3, 2, 1])) # ➞ [5, 5, 5, 5, 5]