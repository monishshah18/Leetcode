class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            st_nums = str(nums[i])
            if st_nums in d:
                if (i-d[st_nums] <= k):
                    return True
                else:
                    d[st_nums] = i
            else:
                d[st_nums] = i
        return False