class Solution:
    def arrangeCoins(self, n: int) -> int:
        low,high = 1,n
        while low <= high:
            mid = (low+high)//2
            total = mid*(mid+1)//2
            if total == n:
                return mid
            elif total > n:
                high = mid - 1
            else:
                low = mid + 1
        return high
        