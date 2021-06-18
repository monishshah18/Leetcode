class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([0])
        n = len(nums)
        ans = []
        for i in range(n):
            while dq and nums[dq[-1]] <= nums[i]: 
                dq.pop()
            dq.append(i)
            if i+1 >= k:
                ans.append(nums[dq[0]])
                if i -dq[0]+1 >=k:
                    dq.popleft()
        return ans