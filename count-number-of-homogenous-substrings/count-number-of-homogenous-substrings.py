class Solution:
    def countHomogenous(self, s: str) -> int:
        def sum_of_subs(n):
            return (n*(n+1))//2
        n = 1
        counter = 0
        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                n += 1
            else:
                counter += sum_of_subs(n)
                n = 1
        counter += sum_of_subs(n)
        return counter%(10**9+7)
                
        