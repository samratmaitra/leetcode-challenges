"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # option 1: O(n) complexity using for loop and check
        # ========================
        # ref_lst = []
        # for num in nums:
        #     if num in ref_lst:
        #         return True
        #     else:
        #         ref_lst.append(num)
        # return False
        #
        # option 2: Load the list into a set to get unique set of numbers and then compare their lengths
        # ========================
        return len(nums) > len(set(nums))
