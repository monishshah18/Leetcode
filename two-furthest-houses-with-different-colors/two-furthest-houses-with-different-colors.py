class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # i,j = 0, len(colors)-1
        # while colors[0]==colors[j]:
        #     j -= 1
        # while colors[-1]==colors[i]:
        #     i += 1
        # return max(len(colors)-1-i,j)
        res = 0
        for i,j in enumerate(colors):
            if j != colors[0]:
                res = max(res, i)
            if j != colors[-1]:
                res = max(res, len(colors)-1-i)
        return res