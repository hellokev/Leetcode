class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupe = {}
        for i in nums:
            if i not in dupe:
                dupe[i] = 1
            elif i in dupe:
                return True
        return False

