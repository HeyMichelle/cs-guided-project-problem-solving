"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid" 
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
- Actually, return an empty list if n <= 0, for the edgecase of if n is -1, or return invalid
"""

# U.P.E.R Planning
# Understand
    # ask ?'s
    # inputs / outputs
    # list of nums
    # number of items from end of list
# Outputs:
        # list or invalid
# Edgecases
        #  invalid if n ? len of list
        #  [] if n = 0

# PLAN
    # Pseudo-code
    # Plain english (don't move on until you can explain it in this way)

    # Where to start?
        # 1. could start with edge cases, how do we handle them?
        # a. invalid if n > length of list
        # b. [] if n = 0
            
    # How to do the main problem?
        # 	1. Get last n of elements of list
            # a. slice
            # b. [ : ]
            # same as "get all elements starting at len -n
                # arr[len(arr)-n: ]

def last(arr, n):
    if n > len(arr):
        return 'invalid'
    elif n == 0:
        return []
    # main solution
    return arr[len(arr) - n : ]
    # return arr[ -n : ] also works

print(last([1, 2, 3, 4, 5], 1))
print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7)) # invalid
print(last([1, 2, 3, 4, 5], 0))
