class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.lst = sorted(nums, reverse=True)
        self.k = k
        

    def add(self, val: int) -> int:
        self.lst.insert(self.BS(val), val)
        return self.lst[self.k - 1]
    
    def BS(self, val):
        left, right = 0, len(self.lst) - 1
        while left <= right:
            mid = (left + right)// 2
            if self.lst[mid]==val:
                return mid
            if self.lst[mid] > val:
                left = mid + 1
            else:
                right = mid - 1
        return left
                


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)