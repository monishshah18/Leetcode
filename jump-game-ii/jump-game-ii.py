class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums)-1
        start,end,step = 0,0,0
        while end < target:
            step += 1
            max_end = end+1
            for i in range(start, end+1):
                if i + nums[i] >= target:
                    return step
                max_end = max(max_end , i+nums[i])
            start, end = end+1, max_end
        return step
        