class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for i,j in enumerate(s):
            if i&1 == int(j):
                count += 1
        return min(count, len(s)-count)