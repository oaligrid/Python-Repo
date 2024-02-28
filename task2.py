#Personal Property of Owais Ali
def min_max_from_unique(nums):
    
    unique_nums = list(set(nums))
    
    
    unique_tuple = tuple(unique_nums)
    
   
    min_num = min(unique_nums)
    max_num = max(unique_nums)
    
    return unique_tuple, min_num, max_num
nums = input("Enter a list of integers separated by commas: ").split(',')
nums = [int(num) for num in nums]
unique_tuple, min_num, max_num = min_max_from_unique(nums)
print("Unique tuple:", unique_tuple)
print("Minimum number:", min_num)
print("Maximum number:", max_num)

