class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = "".join(str(ord(i)-96) for i in s)
        for _ in range(k):
            res = sum(int(i) for i in s)
            s = str(res)
        return res
        