"""
LeetCode 14: Longest Common Prefix
Topic: String, Array, Vertical Scanning
Difficulty: Easy
Link: https://leetcode.com/problems/longest-common-prefix/

Strategy:
- Sort the array of strings to easily compare the most different strings (first and last)
- Iterate character by character through the first string
- Compare each character with the corresponding character in the last string
- Build the prefix until characters don't match, then return the accumulated prefix

Note: The sorting approach works because if the first and last strings in sorted order share a prefix,
all intermediate strings must also share that prefix due to lexicographical ordering.

Complexity:
- Time: O(n log n + m) where n is number of strings and m is length of common prefix
- Space: O(1) as we only use constant extra space (excluding input and output)

Alternative approaches:
- Horizontal scanning: Compare first string with each subsequent string, reducing prefix gradually
- Vertical scanning: Compare all strings character by character from left to right
- Divide and conquer: Split array and find common prefixes recursively, then combine results
- Trie data structure: Build a trie of all strings and find the deepest node with single child
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        strs.sort()
        prefix = ""
        n = len(strs)
        
        for i in range(len(strs[0])):
            if strs[0][i] == strs[n-1][i]:
                prefix += strs[0][i]
            else:
                break
        return prefix