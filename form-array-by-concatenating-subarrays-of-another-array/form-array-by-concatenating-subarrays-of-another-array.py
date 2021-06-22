class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        for grp in groups:
            for j in range(i, len(nums)):
                if nums[j:j+len(grp)] == grp:
                    i = j+len(grp)
                    break
            else:
                return False
        return True
        