class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums)==1: return nums[0]
        
        def f(nums):
            prev, curr = 0,0
            for i in nums:
                temp = curr
                curr = max(curr, prev+i)
                prev = temp
            return curr
        return max(f(nums[:-1]),f(nums[1:]))