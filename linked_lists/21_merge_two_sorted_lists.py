"""
LeetCode 21: Merge Two Sorted Lists
Topic: Linked List, Recursion, Two Pointers
Difficulty: Easy
Link: https://leetcode.com/problems/merge-two-sorted-lists/

Strategy:
- Use iterative approach with a dummy head node to simplify edge cases
- Maintain a tail pointer to build the merged list
- Compare current nodes from both lists and attach the smaller one
- Advance the pointer of the list that contributed the node
- When one list is exhausted, attach the remaining nodes from the other list
- Return head.next (skipping the dummy node)

Note: The iterative approach is efficient with O(1) space complexity. A recursive approach
could also be used but would have O(n+m) space complexity due to call stack.

Complexity:
- Time: O(n + m) where n and m are the lengths of the two lists
- Space: O(1) as we only rearrange existing nodes without allocating new ones (except dummy head)

Alternative approaches:
- Recursive: Compare heads, set next pointer to recursive call with remaining lists
- In-place modification: Merge without dummy node (requires more edge case handling)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head = ListNode()

        tail = head

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 if list1 else list2

        return head.next