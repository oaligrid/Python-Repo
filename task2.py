#Personal Property of Owais Ali
# Given a list of integers. Remove duplicates from the list and create a tuple. Find the minimum and maximum number.
def min_max_from_unique(numbers):
    unique_numbers = list(set(numbers)) 
    unique_tuple = tuple(unique_numbers)  
    min_number = min(unique_tuple)  
    max_number = max(unique_tuple)  
    return min_number, max_number

# Example usage:
numbers = [1, 3, 5, 3, 7, 9, 1, 5]
min_num, max_num = min_max_from_unique(numbers)
print("Minimum number:", min_num)
print("Maximum number:", max_num)

