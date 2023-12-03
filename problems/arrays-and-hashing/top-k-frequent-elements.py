"""
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Get the num and its count of occurances.
        # Store the num as key and the count of occurances as value in a hash map.
        # Find the top-k max values from the hash table and retrieve their keys.
        res_map = dict()
        for num in nums:
            if num in res_map:
                res_map[num] += 1
            else:
                res_map[num] = 1
        print(res_map)
        top_k_freqs = set(sorted(res_map.values())[::-1][:k])
        print(top_k_freqs)
        ans = []
        for freq in top_k_freqs:
            for k,v in res_map.items():
                if freq ==  v:
                    ans.append(k)
        return ans
