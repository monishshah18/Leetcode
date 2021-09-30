class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = None
        for i,j in enumerate(self.nums):
            if j==target:
                count += 1
                chance = random.randint(1,count)
                if chance==count:
                    res = i
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)