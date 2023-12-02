"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def helper(self, ip_str: str) -> dict:
        result_map = dict()
        for char_key in ip_str:
            if char_key not in result_map:
                result_map[char_key] = 1
            else:
                result_map[char_key] += 1
        return result_map

    def isAnagram(self, s: str, t: str) -> bool:
        # Option 1: Compare sorted value of src and tgt strs.
        # ==================================
        # return sorted(list(s)) == sorted(list(t))
        #
        # Option 2: Load the char and their counts in a dictionary using helper method
        # compare the result_map of both src and tgt strs.
        # ==================================
        result_map_s = self.helper(s)
        result_map_t = self.helper(t)
        return result_map_s == result_map_t
