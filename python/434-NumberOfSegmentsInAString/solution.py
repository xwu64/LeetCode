class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        seg = s.split(' ')

        result = 0

        for each in seg:
            if len(each) != 0:
                result+=1

        return result
