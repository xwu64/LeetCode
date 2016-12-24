class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        segments = input.split('\n')
        result = 0

        dirLen = []

        for i, seg in enumerate(segments):

            if '.' in seg:
                print dirLen
                result = max(result, sum(dirLen)+len(seg))
                if i+1 < len(segments):
                    if seg.count('\t') < segments[i+1].count('\t'):
                        dirLen.append(len(seg)-seg.count('\t'))
                    elif seg.count('\t') > segments[i+1].count('\t'):
                        for each in range(seg.count('\t') - segments[i+1].count('\t')):
                            dirLen.pop()
            else:
                if i+1 < len(segments):
                    if seg.count('\t') < segments[i+1].count('\t'):
                        dirLen.append(len(seg)-seg.count('\t'))
                    elif seg.count('\t') > segments[i+1].count('\t'):
                        for each in range(seg.count('\t') - segments[i+1].count('\t')):
                            dirLen.pop()

        return result


