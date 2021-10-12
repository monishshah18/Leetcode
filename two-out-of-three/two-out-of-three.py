class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        n1,n2,n3 = set(nums1), set(nums2), set(nums3)
        return (n1&n2) | (n3&n2) | (n3&n1)
        
        