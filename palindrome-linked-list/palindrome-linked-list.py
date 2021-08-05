# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, rev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            temp = rev
            rev = slow
            slow = slow.next
            rev.next = temp
        if fast:
            slow = slow.next
        while rev:
            if rev.val != slow.val:
                return False
            rev = rev.next
            slow = slow.next
        return True