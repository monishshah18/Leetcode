class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        B =  [j-i for i,j in zip(nums, nums[1:])]
        return sum(((2*len(list(j))-1)**2-1)//8 for i, j in groupby(B))