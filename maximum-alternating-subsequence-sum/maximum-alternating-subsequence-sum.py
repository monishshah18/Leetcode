class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        direction = 'down' #boolean flag
        n = len(nums)
        ans = 0
        for i in range(n-1):
            if direction == 'down' and nums[i] >= nums[i+1]:
                ans += nums[i]
                direction = 'up'
            elif direction == 'up' and nums[i] <= nums[i+1]:
                ans -= nums[i]
                direction = 'down'
        if direction == 'up':
            return ans
        return ans + nums[-1]