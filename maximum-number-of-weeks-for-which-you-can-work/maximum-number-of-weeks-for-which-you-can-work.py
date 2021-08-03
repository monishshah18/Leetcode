class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones_sum = sum(milestones)
        max_milestones = max(milestones)
        if (milestones_sum - max_milestones) >= max_milestones:
            return milestones_sum
        return 2*(milestones_sum-max_milestones) + 1