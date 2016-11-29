class Solution(object):
    def minMoves2(self, nums):
       if len(nums) % 2 == 0:
            low = nums[len(nums)/2-1]
            high = nums[len(nums)/2]
            r1 = 0
            for each in nums:
                r1 += abs(each - low)
                
            r2 = 0
            for each in nums:
                r2 += abs(each - high)
                
            return min(r1, r2)
            
        if len(nums) % 2 == 1:
            mid = nums[len(nums)/2]
            result = 0
            for each in nums:
                result += abs(each - mid)
            return result
