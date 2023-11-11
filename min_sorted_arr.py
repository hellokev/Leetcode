class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: #check if m is part of left sorted portion
                l = m + 1 #if it is, then search right
            else:
                r = m - 1 #search left
        return res

        # 3 4 5 1 2
        # 1.
        # l = 0, r = 4
        # m = (0 + 4) // 2 = 2
        # res = min(3, 5) = 3
        # if nums[2] is 5 > = nums[0] is 3:
        # l = 2 + 1 = 3
        
        # 2.
        # l = 3, r = 4
        # m = ( 3 + 4 ) // 2 = 3
        # res = min(3, 1) = 1
        # if nums[3] >= nums[3]
        # l = 3 + 1 = 4

        # 3.
        # l = 4 , r = 4
        # m = ( 4 + 4 ) // 2 = 4
        # res = min(1, 2) = 1
        # if nums[4] >= nums[2]:
        # l = 4 + 1 = 5 

        #break out of loop return res