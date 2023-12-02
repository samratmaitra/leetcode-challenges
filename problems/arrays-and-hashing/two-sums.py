"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def helper(self, nums:list[int]) -> dict:
        result_map = dict()
        for idx, num in enumerate(nums):
            if num not in result_map:
                result_map[num] = [idx]
            else:
                result_map[num].append(idx)
        return result_map

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Option 1: Nested loop Approach
        # ========================================
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        #
        # Option 2: Load the numbers and their indices into a hash map. 
        # Run single loop and search the second index from the hash map.
        # ========================================
        result_map = self.helper(nums)
        for i in range(len(nums)):
            if (target-nums[i]) in result_map:
                for j in result_map[(target-nums[i])]:
                    if i != j:
                        return [i,j]
