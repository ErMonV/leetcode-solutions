"""
LeetCode 9: Palindrome Number
Topic: Math / String Conversion
Difficulty: Easy
Link: https://leetcode.com/problems/palindrome-number/

Strategy:
- Convert integer to string for easy character comparison
- Check if the string equals its reverse using slicing [::-1]

Note: This approach uses string conversion which is acceptable for this problem
but there's also a mathematical approach without string conversion.

Complexity:
- Time: O(n) where n is the number of digits.
- Space: O(n) for the string conversion

Alternative approach:
- Reverse the number mathematically and compare with original
- Avoids string conversion but has similar time complexity
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        return str(x) == str(x)[::-1]