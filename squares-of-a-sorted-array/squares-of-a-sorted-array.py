class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        right_pointer = len(nums)-1
        left_read_pointer = 0
        right_read_pointer = len(nums)-1
        left_sq = nums[left_read_pointer]**2
        right_sq = nums[right_read_pointer]**2
        while right_pointer >= 0:
            if left_sq > right_sq:
                res[right_pointer] = left_sq
                left_read_pointer += 1
                left_sq = nums[left_read_pointer]**2
            else:
                res[right_pointer] = right_sq
                right_read_pointer -= 1
                right_sq = nums[right_read_pointer]**2
            right_pointer -= 1
        return res