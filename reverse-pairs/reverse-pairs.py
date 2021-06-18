class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        new_list = []
        result = 0
        for i in range(len(nums)):
            temp = bisect.bisect_right(new_list, 2*nums[i])
            result += len(new_list) - temp
            bisect.insort(new_list,nums[i])
        return result
        