"""1.1 Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

input [1,2,3,4,5]
output [120,60,40,30,24]

input [3,2,1]
output [2,3,6]

**No division**
"""

# create prefix and suffix, for prefix: starting with 1; for suffix, ending with value 1; do not include ith element itself.


def product_of_i_version2(arr):
    
    prefix = []
    suffix = []
    
    prefix_total = 1
    suffix_total = 1
    
    for i in range(len(arr)):
          
        if i == 0:
            prefix.append(1)
        else:
            prefix_total *= arr[i-1]
            prefix.append(prefix_total)
            
    reversed_arr = arr[::-1]
    
            
    for i in range(len(arr)):
        
        if i==0:
            suffix.append(1)
        else:
            suffix_total *= reversed_arr[i-1]
            suffix.append(suffix_total)
            
    suffix_r = suffix[::-1]
        
    output =[]
    
    for i in range(len(arr)):
            
            output.append(prefix[i]*suffix_r[i])
        
    return output
