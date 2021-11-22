class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i,j = 0, len(colors)-1
        while colors[0]==colors[j]:
            j -= 1
        while colors[-1]==colors[i]:
            i += 1
        return max(len(colors)-1-i,j)