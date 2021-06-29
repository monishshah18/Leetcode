class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans, l = 0, 0
        n = len(nums)
        for r in range(n):
            if nums[r] == 0:
                if k == 0:
                    while(nums[l] != 0): l += 1
                    l += 1
                else: k -= 1
                    
            ans = max(ans, r-l+1)
        return ans
        