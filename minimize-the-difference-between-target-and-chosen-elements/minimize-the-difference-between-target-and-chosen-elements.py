class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        possible_min = sum(min(i) for i in mat)
        if possible_min > target: return possible_min - target
        nums = {0}
        for row in mat:
            nums = {x+i for x in row for i in nums if x + i <= 2*target - possible_min}
        return min(abs(target-x) for x in nums)