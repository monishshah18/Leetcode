class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = 2 * ((low+high)//4)
            if nums[mid] == nums[mid+1]:
                low = mid + 2
            else:
                high = mid
        return nums[low]