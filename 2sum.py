class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newDict = {}
        for key, val in enumerate(nums):
            diff = target - val 
            if diff in newDict:
                return newDict[diff], key
            else:
                newDict[val] = key