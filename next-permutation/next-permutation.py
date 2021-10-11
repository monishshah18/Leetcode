class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.nums = nums
        i = self.find_decreasing()
        if i >= 0:
            j = self.find_increasing(i)
            self.swap(i,j)
        self.reverse(start=i+1)
        
    def find_decreasing(self):
        i = len(self.nums) - 2
        while i >= 0:
            if self.nums[i] < self.nums[i+1]:
                break
            i -= 1
        return i
    def find_increasing(self, i):
        num = self.nums[i]
        j = len(self.nums)-1
        while j >= 0:
            if self.nums[j] > num:
                break
            j -= 1
        return j
    def swap(self,i,j):
        self.nums[i],self.nums[j] = self.nums[j],self.nums[i]
    def reverse(self, start):
        i = start
        j = len(self.nums)-1
        while i < j:
            self.swap(i,j)
            i += 1
            j -= 1