def find_missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

# Example usage:
nums = [3, 0, 1]
missing_number = find_missing_number(nums)
print(f"The missing number is: {missing_number}")