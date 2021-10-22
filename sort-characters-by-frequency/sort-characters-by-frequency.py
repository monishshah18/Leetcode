class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([i*j for i,j in Counter(s).most_common()])