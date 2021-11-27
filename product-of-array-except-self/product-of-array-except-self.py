class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]*len(nums)
        leftProduct = 1
        for i in range(1, len(nums)):
            leftProduct *= nums[i-1]
            products[i] = leftProduct
        
        rightProduct = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= rightProduct
            rightProduct *= nums[i]
        return products
            