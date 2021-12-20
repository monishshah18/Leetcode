class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = min((j-i) for i,j in zip(arr, arr[1:]))
        res = [[a,b] for a,b in zip(arr, arr[1:]) if b-a == min_diff]
        return res