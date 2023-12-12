"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = list(set(nums))
        if not len(nums):
            return 0
        nums.sort()
        val = 1
        vals = []
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                val += 1
            else:
                vals.append(val)
                val = 1
        vals.append(val)
        val = 1
        return max(vals)
