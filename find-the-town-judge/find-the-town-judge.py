class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = {}
        for p in range(1, n+1):
            trust_count[p] = 0
        for trustor, trustee in trust:
            trust_count[trustor] -= 1
            trust_count[trustee] += 1
        for p, trust_person_count in trust_count.items():
            #print(p,trust_person_count)
            if trust_person_count == n - 1:
                return p
        return -1