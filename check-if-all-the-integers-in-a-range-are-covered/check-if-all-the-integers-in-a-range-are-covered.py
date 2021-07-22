class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        temp = [0]*(60)
        for i in ranges:
            temp[i[0]] += 1
            temp[i[1]+1] -= 1
        for i in range(1, len(temp)):
            temp[i] += temp[i-1]
        return min(temp[left:right+1]) >= 1