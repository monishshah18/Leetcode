class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        count = 0
        dic = {min(i,j):max(i,j) for i,j in zip(row[0::2],row[1::2])}
        for i in range(0, len(row), 2):
            temp = dic[i]
            if abs(i-temp) > 1:
                count += 1
                d = dic.pop(i+1)
                dic[min(temp, d)], dic[i] = max(temp,d), i+1
        return count
        
        