class MinStack:
    class ListNode:
        def __init__(self):
            self.val = val
            self.next = next

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smallest = None
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.smallest or val <= self.smallest.val:
            l = ListNode(val, next = self.smallest)
            self.smallest = l

    def pop(self) -> None:
        p = self.stack.pop()
        if self.smallest and self.smallest.val == p:
            self.smallest = self.smallest.next

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest.val if self.smallest else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()