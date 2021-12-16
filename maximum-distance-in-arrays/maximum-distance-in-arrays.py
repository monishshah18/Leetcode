class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        global_max, index_max = max((arr[-1], index) for index, arr in enumerate(arrays))
        global_min, index_min = min((arr[0], index) for index,arr in enumerate(arrays))
        if index_min != index_max:
            return global_max - global_min
        sec_max, index_sec = max((arr[-1], index) for index,arr in enumerate(arrays) if index != index_max)
        sec_min, index_sec = min((arr[0], index) for index, arr in enumerate(arrays) if index != index_min)
        return max(abs(global_max - sec_min), abs(global_min - sec_max))