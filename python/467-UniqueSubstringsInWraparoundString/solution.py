class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """

        if len(p) == 0:
            return 0
        result = len(set(p))
        segments = []

        start = i = 0
        maxlen = 0
        while 1:
            if i+1 == len(p):
                maxlen = max(maxlen, i+1-start)
                segments.append(p[start:i+1])
                break
            if ord(p[i+1]) - ord(p[i]) != 1:
                if ord(p[i+1]) - ord(p[i]) != -25:
                    maxlen = max(maxlen, i+1-start)
                    segments.append(p[start:i+1])
                    start = i+1
                    i = i+1
                    continue
            i+=1
        i=2
        while i<=maxlen:
            candidates = []

            for seg in segments:
                if len(seg) < i:
                    continue

                if len(seg) > 26+i:
                    candidates = []
                    result += 26
                    break

                for item in range(len(seg)-i+1):
                    candidates.append(seg[item:item+i])

            result += len(set(candidates))
            i+=1
        return result
