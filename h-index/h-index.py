class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        n = len(citations)
        citations.sort(reverse=True)
        i = 0
        while i < n and citations[i] > i:
            i += 1
        return i
        