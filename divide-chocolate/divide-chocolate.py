class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def divide(target):
            count, _sum = 0,0
            for s in sweetness:
                _sum += s
                if _sum >= target:
                    count += 1
                    _sum = 0
            return count
        low, high = min(sweetness), sum(sweetness)//(k+1)
        while low < high:
            mid = (low+high+1)//2
            if divide(mid) < k+1:
                high = mid - 1
            else:
                low = mid
        return low