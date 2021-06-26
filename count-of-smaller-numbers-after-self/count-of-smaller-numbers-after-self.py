class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0]*len(nums)
        indexes_nums = [(nums[i],i) for i in range(len(nums))]
        desc_nums, counts = self.mergeWithCounts(indexes_nums, counts)
        return counts
    def mergeWithCounts(self, nums, counts):
        if len(nums) == 1:
            return nums, counts
        stack = []
        left, counts = self.mergeWithCounts(nums[:len(nums)// 2], counts)
        right, counts = self.mergeWithCounts(nums[len(nums)//2:], counts)
        while left and right:
            if left[0] > right[0]:
                counts[left[0][1]] += len(right)
                stack.append(left.pop(0))
            else:
                stack.append(right.pop(0))
        if left:
            stack.extend(left)
        else:
            stack.extend(right)
        return stack, counts
        