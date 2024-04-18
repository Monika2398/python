'''def reverse_string(input_str):
    return input_str[::-1]
input_str = input().strip()
print(reverse_string(input_str))'''

'''def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
    i += 6 
    return True
number = int(input())
if is_prime(number):
    print("yes")
else:
    print("no")'''

'''def largest_number(nums):
    nums = list(map(str,nums))
    def compare(a,b):
        return int(b + a) - int(a + b)
    nums.sort(key = compare(a,b))
    return ''.join(nums)
input_nums = [54,546,548,60]
print (largest_number(input_nums))'''

'''def largest_number(nums):
    # Convert numbers to strings for easy comparison
    nums = list(map(str, nums))
    
    # Custom comparator function for sorting
    def compare(a, b):
        return int(b + a) - int(a + b)
    
    # Sort the numbers based on the custom comparator
    nums.sort(key=compare)
    
    # Join the sorted numbers into a single string
    return ''.join(nums)

# Input
input_nums = [54, 546, 548, 60]

# Output
print(largest_number(input_nums))'''

'''def largest_number(nums):
    # Custom comparator function for sorting
    def compare(a, b):
        return int(b + a) - int(a + b)
    
    # Convert numbers to strings for easy comparison
    nums_str = [str(num) for num in nums]
    
    # Join the sorted numbers into a single string
    return ''.join(nums_str)

# Input
input_nums = [54, 546, 548, 60]

# Output
print(largest_number(input_nums))'''

'''def largest_number(nums):
    # Convert numbers to strings for easy comparison
    nums_str = list(map(str, nums))
    
    # Custom comparison function for sorting
    def compare(a, b):
        # Concatenate and compare the two numbers in different orders
        return int(b + a) - int(a + b)
    
    # Sort the numbers based on the custom comparison
    nums_str.sort(key=lambda x: compare(x, x))
    
    # Join the sorted numbers into a single string
    return ''.join(nums_str)

# Example usage:
input_nums = [54, 546, 548, 60]
print(largest_number(input_nums))'''

'''def largest_number(nums):
    # Convert numbers to strings for easy comparison
    nums_str = list(map(str, nums))
    
    # Custom comparison function for sorting
    def compare(a, b):
        # Concatenate and compare the two numbers in different orders
        return int(b + a) - int(a + b)
    
    # Sort the numbers based on the custom comparison
    nums_str.sort(key=lambda x: compare(x, x))
    
    # Join the sorted numbers into a single string
    return ''.join(nums_str)

# Input
input_nums = [54, 546, 548, 60]

# Output
print(largest_number(input_nums))'''

'''N = int(input("Enter a number: "))
reverse_N = int(str(N)[::-1])
print(reverse_N)'''

'''def find_max_min(arr):
    if not arr:
        return None, None

    max_num = arr[0]
    min_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num

# Example usage
arr = [54, 546, 548, 60]
max_num, min_num = find_max_min(arr)
print(max_num, min_num)'''

from functools import cmp_to_key

def largest_number(arr):
    # Custom comparison function to compare two numbers as strings
    def compare(a, b):
        return int(b + a) - int(a + b)

    # Convert numbers to strings and sort them using the custom comparison function
    sorted_arr = sorted(map(str, arr), key=cmp_to_key(compare))

    # Concatenate the sorted strings to form the largest number
    largest_num = ''.join(sorted_arr)

    return largest_num

# Example usage
arr = [54, 546, 548, 60]
largest_num = largest_number(arr)
print(largest_num)
