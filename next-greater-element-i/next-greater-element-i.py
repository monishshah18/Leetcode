class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        
        for i,j in list(enumerate(nums1)):
            index = nums2.index(j)
            flag = False
            for i in range(index, len(nums2)):
                if nums2[i] > j:
                    res.append(nums2[i])
                    flag = True
                    break
            if not flag:
                res.append(-1)
        return res