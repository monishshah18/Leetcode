class Solution:
    def uniqueLetterString(self, s: str) -> int:
        prev =  ans = 0
        dict = {}
        for i, j in enumerate(s):
            k, c = dict.get(j, [-1,-1])
            prev =  prev + (i-c)-(c-k)
            dict[j] = [c,i]
            ans += prev
        return ans
        