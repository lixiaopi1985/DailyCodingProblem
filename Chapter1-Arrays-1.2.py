"""
1.2 **Locate smallest window to be sorted**


Given an array of integers that are out of order, determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted. For example:

input [3,7,5,6,9]
ouput (1,3)
"""


def smallest_window(arr):
    
    prev = 0
    bound = []
    max_unordered = 0
    
    for i in range(len(arr)):
        
        if arr[i] < prev:
            bound.append(i)

            if arr[i-1] > max_unordered:
                max_unordered = arr[i-1]
                
        prev = arr[i]
        
    upper = 0
    for i in range(len(arr)):
        if arr[i] > max_unordered:
            upper = i - 1

    lower = bound[0] - 1
        
    return lower, upper
