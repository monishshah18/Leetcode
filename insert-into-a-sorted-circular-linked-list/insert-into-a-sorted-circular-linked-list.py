"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode
        if head.next == head:
            head.next = Node(insertVal, head)
            return head
        
        lptr = head
        rptr = head.next
        x = insertVal
        #more than 2 elements in the list
        
        while lptr.next!=head:
            if lptr.val <=rptr.val:
                if x>=lptr.val and x<=rptr.val:
                    lptr.next = Node(x)
                    lptr.next.next = rptr
                    return head
            else:
                if x>=lptr.val or x<=rptr.val: 
                    lptr.next = Node(x)
                    lptr.next.next = rptr
                    return head
            lptr = lptr.next
            rptr = rptr.next
        if lptr.val <=rptr.val:
            if x>=lptr.val and x<=rptr.val:
                lptr.next = Node(x)
                lptr.next.next = rptr
                return head
        else:
            if x>=lptr.val or x<=rptr.val: 
                lptr.next = Node(x)
                lptr.next.next = rptr
                return head

        
        # insert initially
        lptr.next = Node(insertVal, head)
        lptr.next.next = rptr
        return head
            