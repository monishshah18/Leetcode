class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, i, j):
        if i==j:
            return nums[i]
        if nums[i] < nums[j]:
            return nums[i]
        else:
            mid = (i+j)//2
            left_min = self.helper(nums,i,mid)
            right_min = self.helper(nums, mid+1, j)
            return min(left_min, right_min)