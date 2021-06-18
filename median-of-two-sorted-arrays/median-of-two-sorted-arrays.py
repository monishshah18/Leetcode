class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums = list(sorted(nums))
        nums_len = len(nums)
        mid = 0
        new_nums = []
        if nums_len%2 == 0:
            mid = nums_len//2
            new_nums.append(nums[mid-1])
            new_nums.append(nums[mid])
            b = sum(new_nums)
            return float(b/2)
        else:
            mid = nums_len//2
            return float(nums[mid])