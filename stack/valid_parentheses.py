"""
LeetCode 20: Valid Parentheses
Topic: String, Stack
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Strategy:
- Use a stack data structure to keep track of opening brackets
- Iterate through each character in the string
- When encountering an opening bracket '(', '[', or '{', push it onto the stack
- When encountering a closing bracket ')', ']', or '}', check if it matches the top of the stack
- If it matches, pop from the stack; if not, return False immediately
- After processing all characters, check if the stack is empty (all brackets were properly closed)

Note: The stack approach ensures that brackets are closed in the correct order (LIFO principle)

Complexity:
- Time: O(n) where n is the length of the string
- Space: O(n) in worst case (when all characters are opening brackets)

Alternative approaches:
- Recursive elimination: Repeatedly remove valid pairs until string is empty (less efficient)
- Counter approach: Doesn't work for order validation, only counts (insufficient for this problem)
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack: # if we encounter a closing bracket but stack of open brackets is empty
                    return False
                
                if (char == ')' and stack[-1] == '(') or \
                    (char == ']' and stack[-1] == '[') or \
                    (char == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0