class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        count = 0
        if k == 0:
            for i,j in d.items():
                if j > 1:
                    count += 1
        else:
            for i,j in d.items():
                if (i+k) in d:
                    count += 1
                    
        return count
        