# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(l1=None, l2=None):
            if not l1 or l2 and l1.val > l2.val: l1,l2 = l2,l1
            if l1: l1.next = merge(l1.next, l2)
            return l1
        return merge(self.mergeKLists(lists[:len(lists)//2]), self.mergeKLists(lists[len(lists)//2:])) if len(lists) > 2 else merge(*lists)