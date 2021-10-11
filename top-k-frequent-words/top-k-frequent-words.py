class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ct = Counter(words)
        heap = heapq.nsmallest(k, ct.items(), lambda item: (-item[1],item[0]))
        return [word for word,_ in heap]