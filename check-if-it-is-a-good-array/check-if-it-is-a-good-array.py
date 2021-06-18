import math
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        val = nums[0]
        for i in range(1, len(nums)):
            val = math.gcd(val, nums[i])
        if val == 1:
            return True
        return False
        
        