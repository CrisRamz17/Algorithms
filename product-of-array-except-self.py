def product_except_self(nums):
    length = len(nums)
    answer = [0] * length

    # answer[i] contains the product of all the elements to the left of i
    answer[0] = 1
    for i in range(1, length):
        # Calculate the product of elements to the left of index i
        answer[i] = nums[i - 1] * answer[i - 1]

    # R contains the product of all the elements to the right of i
    R = 1
    for i in reversed(range(length)):
        # Multiply with the product of elements to the right of index i
        answer[i] = answer[i] * R
        # Update R to include the current element
        R *= nums[i]

    return answer

# Example usage:
nums = [1, 2, 3, 4, 5]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]