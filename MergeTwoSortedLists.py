"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MergeTwoSortedLists:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer: ListNode = ListNode(-1)
        temp = answer
        while l1 or l2:
            if not l1:
                temp.next = l2
                return answer.next
            elif not l2:
                temp.next = l1
                return answer.next
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        return answer.next
