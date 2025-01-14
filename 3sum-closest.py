from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf')
        
        for i in range(len(nums) - 2):            
            left = i + 1
            right = len(nums) - 1            
            while left < right:                
                currSum = nums[i] + nums[left] + nums[right]                
                if currSum == target:
                    return currSum
                if abs(currSum - target) < abs(result - target):
                    result = currSum
                if currSum < target:
                    left += 1
                else:
                    right -= 1
        return result

# Example usage: 
nums = [-1, 2, 1, -4]
target = 1
print(Solution().threeSumClosest(nums, target))  # Output: 2
