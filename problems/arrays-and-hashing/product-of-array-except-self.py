"""
Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        val = 1
        l_scan = []
        r_scan = []

        # Compute rolling multiplier from the left except the element.
        for num in nums:
            l_scan.append(val)
            val *= num
        
        # Compute rolling multiplier from the right except the element.
        val = 1
        for num in nums[::-1]:
            r_scan.append(val)
            val *= num
            
        r_scan = r_scan[::-1]

        # return a list of element wise multiplication of l_scan and r_scan
        return [i*j for i,j in zip(l_scan, r_scan)]
