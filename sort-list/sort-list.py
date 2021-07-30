# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p, slow, fast = None, head, head
        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next
        p.next = None
        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self, l1, l2):
        temp = ListNode(None)
        curr = temp
        while l1 and l2:
            if l1.val > l2.val:
                curr.next,l2 = l2, l2.next
            else:
                curr.next,l1 = l1, l1.next
            curr = curr.next
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        return temp.next