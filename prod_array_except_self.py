class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        print(result)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            print(i)
            result[i] *= postfix 
            postfix *= nums[i]
        return result