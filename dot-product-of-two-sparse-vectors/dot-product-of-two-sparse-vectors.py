class SparseVector:
    def __init__(self, nums: List[int]):
        self.seen = {}
        for i,j in enumerate(nums):
            if j != 0:
                self.seen[i] = j
    
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i,n in vec.seen.items():
            if i in self.seen:
                res += n*self.seen[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)