class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        N = len(s1)
        def dfs(A, B, pos):
            sB = ''.join(B)
            if sB in sMap:
                return sMap[sB]
            if A == B:
                return 0
            while A[pos] == B[pos]:
                pos += 1
            minCnt = float('inf')
            for i in range(pos+1, N):
                if B[i]==A[pos] and B[i]!=A[i]:
                    B[i], B[pos] = B[pos], B[i]
                    temp = dfs(A, B, pos+1) + 1
                    minCnt = min(minCnt, temp)
                    B[i], B[pos] = B[pos], B[i]
            sMap[sB] = minCnt
            return minCnt
                    
        sMap = collections.defaultdict()
        return dfs(list(s1), list(s2), 0)