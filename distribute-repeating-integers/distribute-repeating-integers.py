class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freq_dict = {}
        for x in nums: freq_dict[x] = 1+freq_dict.get(x,0)
        val = sorted(freq_dict.values(), reverse=True)
        quantity.sort(reverse=True)
        def f(i):
            if i == len(quantity): return True
            seen = set()
            for j in range(len(val)):
                if val[j] >= quantity[i] and val[j] not in seen:
                    seen.add(val[j])
                    val[j] -= quantity[i]
                    if f(i+1): 
                        return True
                    val[j] += quantity[i]
        return f(0)
        