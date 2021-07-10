class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t==0 and len(set(nums))==len(nums):
            return False
        n = len(nums)
        width = t + 1
        bucket = {}
        for i,j in enumerate(nums):
            bucket_idx = j // width
            if bucket_idx in bucket:
                return True
            elif bucket_idx + 1 in bucket and abs(j-bucket[bucket_idx+1]) < width:
                return True
            elif bucket_idx - 1 in bucket and abs(j-bucket[bucket_idx-1]) < width:
                return True
            bucket[bucket_idx] = j
            if i >= k:
                del bucket[nums[i-k]//width]
        return False
        
        