"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, 
or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution:
    def reverse(self, l: list) -> list:
        i, j = 0, len(l)-1
        while i < j:
            tmp = l[i]
            l[i] = l[j]
            l[j] = tmp
            i += 1
            j -= 1
        return l

    def lst2str(self, l: list) -> str:
        op_str = ""
        for c in l:
            op_str += c
        return op_str

    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ","")
        l = [c for c in s if (ord(c)>=97 and ord(c)<=122) or (ord(c)>=48 and ord(c)<=57)]
        return self.lst2str(l) == self.lst2str(self.reverse(l))
