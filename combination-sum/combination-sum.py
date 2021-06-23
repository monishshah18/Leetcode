class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        dp = {}
        dp[0] = [[]]
        for candidate in candidates:
            for i in range(candidate, target+1):
                combinations = dp.get(i-candidate, [])
                dp.setdefault(i,[])
                for comb in combinations:
                    dp[i].append(comb + [candidate])
        return dp.get(target, [])
        