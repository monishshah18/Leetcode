class Solution:
    def findLHS(self, nums: List[int]) -> int:
        no_of_occurences = Counter(nums)
        max_len = 0
        for i in no_of_occurences:
            if (i-1) in no_of_occurences:
                curr_len = no_of_occurences[i]+no_of_occurences[i-1]
                max_len = max(max_len,curr_len)
        return max_len