class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        ans = [i for i in num]
        num_change = 0
        for i in range(len(num)):
            if change[int(num[i])] > int(num[i]):
                ans[i] = str(change[int(num[i])])
                num_change += 1
            elif change[int(num[i])] == int(num[i]):
                pass
            else:
                if num_change > 0:
                    return "".join(ans)
                else:
                    pass
        return "".join(ans)