class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x:(-x[0],x[1]))
        ans, curr_max = 0,0
        for i,j in properties:
            if j < curr_max:
                ans += 1
            else:
                curr_max = j
        return ans
        