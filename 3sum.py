def three_sum(nums):
    """
    Given an array nums of n integers, this function finds all unique triplets 
    in the array which gives the sum of zero.

    Args:
        nums (List[int]): List of integers.

    Returns:
        List[List[int]]: A list of lists containing triplets that sum up to zero.

    The algorithm works as follows:
    1. Sort the input list.
    2. Iterate through the list with the index `i`.
        - Skip duplicate elements to avoid duplicate triplets.
    3. Use two pointers, `left` and `right`, to find pairs that sum up with nums[i] to zero.
        - If the sum is less than zero, move the `left` pointer to the right.
        - If the sum is greater than zero, move the `right` pointer to the left.
        - If the sum is zero, add the triplet to the result list.
        - Skip duplicate elements for both `left` and `right` pointers.
    4. Return the list of unique triplets.
    """
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]