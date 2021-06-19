class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = [c for c in 'aieouAEIOU']
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] not in vowels:
                l += 1
            if s[r] not in vowels:
                r -= 1
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)
        