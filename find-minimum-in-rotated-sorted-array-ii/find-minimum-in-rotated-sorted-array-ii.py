class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.helper(nums,0,len(nums)-1)
        
    def helper(self,nums, i,j):
        #one element
        if i == j:
            return nums[i]
        #not rotated or rotated len(nums) times, 1st is the minimum
        if nums[i] < nums[j]:
            return nums[i]
        else:
            #now split and find min at the left and right parts, return the min of min
            mid = (i+j)//2
            left_min = self.helper(nums,i, mid)
            right_min = self.helper(nums,mid+1,j)
            return min(left_min,right_min)
        