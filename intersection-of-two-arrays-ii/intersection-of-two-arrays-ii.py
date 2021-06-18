class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        s1 = set(nums1)
        s2 = set(nums2)
        arr = []
        for s in list(s1.intersection(s2)):
            arr.extend(list(repeat(s, min(count1[s], count2[s]))))
        return arr