"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order. An Anagram is a word or phrase 
formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""
class Solution:
    def hash_key(self, str_val:str) -> str:
        op_str = ""
        for c in sorted(str_val):
            op_str += c
        return op_str

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # For every str element, create a hash key by sorting the str value (using the helper method)
        # Store the key in a hash table, assign values for all the strs for which the hash key is the same. 
        # Finally, loop over the hash table and retrieve the values for every key
        result_map = dict()
        for element in strs:
            key = self.hash_key(element)
            if key not in result_map:
                result_map[key] = [element]
            else:
                result_map[key].append(element)
        return [v for v in result_map.values()]
