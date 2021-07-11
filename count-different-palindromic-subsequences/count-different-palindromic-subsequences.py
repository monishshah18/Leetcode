class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 1000000007
        
        @lru_cache(maxsize=None)
        def compute(start: int, end: int) -> int:
            if start >= end:
                return 0
            count = 0
            for ch in "abcd":
                left, right = s.find(ch, start, end), s.rfind(ch, start, end)
                if left == -1 or right == -1:
                    continue
                count += 1 if left == right else 2 + compute(left + 1, right)
                
            return count % MOD
        
        return compute(0, len(s))
        