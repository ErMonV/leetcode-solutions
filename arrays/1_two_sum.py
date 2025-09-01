"""
LeetCode 1: Two Sum
Topic: Arrays / Hash Map
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Strategy:                                                   
- Use a dictionary (hash map) to store seen numbers and their indices.
- In each iteration, calculate the complement (target - current number).
- Check if the complement already exists in the dictionary.
- If found, return the indices of the complement and the current index.
- If not found, add the current number to the dictionary with its index.

Complexity:
- Time: O(n) - We traverse the array only once
- Space: O(n) - Worst case we store all elements in the dictionary

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_dict:
                return [nums_dict[complement], i]
            nums_dict[nums[i]] = i