class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        temp = 0
        for i in arr:
            temp += cnt[i]==1
            if temp==k:
                return i
        return ""
            