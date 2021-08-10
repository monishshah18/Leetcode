class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low,high = 0, len(numbers)-1
        while (s := sum((numbers[low], numbers[high]))) != target:
            if s > target:
                high -= 1
            else:
                low += 1
        return [low+1, high+1]