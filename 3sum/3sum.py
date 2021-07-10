class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        _set = set()
        for i in range(len(nums)):
            if not(i > 2 and nums[i]==nums[i-2]):
                for j in range(i+1, len(nums)):
                    sol = -(nums[i]+nums[j])
                    if sol in _set:
                        res.add((nums[i],nums[j],sol))
                _set.add(nums[i])
        return list(res)
        