"""
LeetCode 13: Roman to Integer
Topic: Hash Table, String, Right-to-Left Processing
Difficulty: Easy
Link: https://leetcode.com/problems/roman-to-integer/

Strategy:
- Use a dictionary to map Roman numerals to their integer values
- Process the string from right to left to handle subtractive notation easily
- For each character, add its value unless it's smaller than the previous value (indicating subtraction)

Note: The right-to-left approach simplifies the logic for cases like IV (4), IX (9), XL (40), etc.
where a smaller numeral precedes a larger one, indicating subtraction.

Complexity:
- Time: O(n) where n is the length of the Roman numeral string
- Space: O(n) due to creating the reversed string slice s[::-1]

Alternative approach:
- Using reversed() iterator for O(1) space complexity
- Left-to-right processing with lookahead to check for subtractive cases
- Mathematical approach without hash table (using if-else chains)
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_integer = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }

        total = 0
        value = 0
        prev_value = 0

        for symbol in s[::-1]:
            value = roman_to_integer[symbol]
            if(value >= prev_value):
                total += value
            else:
                total -= value
            prev_value = value
        return total
