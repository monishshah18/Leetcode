class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def twopass(arr,i,j):
            while i < j:
                arr[i],arr[j] = arr[j],arr[i]
                i += 1
                j -= 1
            return arr
        if k > len(nums):
            k %= len(nums)
        if k > 0:
            twopass(nums, 0, len(nums)-1)
            twopass(nums, 0, k-1)
            twopass(nums, k, len(nums)-1)