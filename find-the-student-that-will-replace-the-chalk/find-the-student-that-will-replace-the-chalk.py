class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_arr = sum(chalk)
        rem = k % sum_arr
        for i in range(len(chalk)):
            rem -= chalk[i]
            if rem < 0:
                return i
        