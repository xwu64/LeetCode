class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0
        dir = {}
        start = 0
        result = 1

        for i, ch in enumerate(s):
            if dir.has_key(ch):
                if dir[ch]<start:
                    dir[ch] = i
                    if i == len(s) -1:
                        result = max(result, i-start+1)
                    continue
                result = max(result, i-start)
                start = dir[ch]+1
                dir[ch] = i
            else:
                dir[ch] = i
                if i == len(s) -1:
                    result = max(result, i-start+1)

        return result
