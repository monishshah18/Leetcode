class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        N = str(n)
        n_len = len(N)
        res = sum(len(digits) ** i for i in range(1, n_len))
        i = 0
        while i < len(N):
            res += sum(c < N[i] for c in digits) * (len(digits) ** (n_len - i - 1))
            if N[i] not in digits: break
            i += 1
        return res + (i == n_len)