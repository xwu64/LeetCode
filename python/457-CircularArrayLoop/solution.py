class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def oneWay(nums):
            for start in xrange(len(nums)):
                if nums[start] <0:
                    continue
                i = start
                while 1:
                    if nums[i] == 0:
                        if nums.count(0) >1:
                            return True
                        else:
                            break

                    if nums[i] < 0:
                        break
                    tmp = nums[i]
                    nums[i] = 0
                    i = (tmp+i)%len(nums)

                for i in range(len(nums)):
                    if nums[i] == 0:
                        nums[i]-=1
            return False

        reverseNums = []
        for each in nums:
            reverseNums.append(-each)

        #print oneWay(nums)
        #print oneWay(reverseNums[::-1])
        return oneWay(nums) or oneWay(reverseNums[::-1])
